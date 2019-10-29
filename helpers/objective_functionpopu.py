from abc import ABC, abstractmethod

import itertools
import numpy as np
import geopandas as gpd

from region.util import get_metric_function

class ObjectiveFunction(ABC):
    def __init__(self, metric=None):
        """
        Parameters
        ----------
        metric : function or str or None, default: None
            Refer to the `metric` argument
            in :func:`region.util.get_metric_function`.
        """
        self.metric = get_metric_function(metric)

    @abstractmethod
    def __call__(self, labels, attr):
        """
        Calculate the objective value given the instance's current data.
        Parameters
        ----------
        labels : :class:`numpy.ndarray`
            The areas' region labels. Shape: number of areas.
        attr : :class:`numpy.ndarray`
            The areas' attributes. Shape: number of areas.

        Returns
        -------
        obj_val : float
            The objective value attained with the clustering defined by
            `labels`.
        """

    @abstractmethod
    def update(self, moving_area, recipient_region, labels, attr):
        """
        Calculate the difference in the objective value caused by moving
        `moving_area` to `recipient_region`.

        Parameters
        ----------
        moving_area : int
            The area to move.
        recipient_region : int
            The recipient region.
        labels : :class:`numpy.ndarray`
            The areas' region labels before the move. Shape: number of areas.
        attr : :class:`numpy.ndarray`
            The areas' attributes. Shape: number of areas.

        Returns
        -------
        diff : float
            The change in the objective function caused by moving `moving_area`
            to `recipient_region`."""

    def natural_weight(self, attr, ndist = 7):
        return 1
    


class ObjectiveFunctionPairwise(ObjectiveFunction):
    def __call__(self, labels, attr):
        """
        Examples
        --------
        >>> from sklearn.metrics.pairwise import distance_metrics
        >>> metric = distance_metrics()["manhattan"]
        >>> labels = np.array([0, 0, 0, 0, 1, 1])
        >>> attr = np.arange(len(labels)).reshape(-1, 1)
        >>> objective = ObjectiveFunctionPairwise(metric)
        >>> int(objective(labels, attr))
        11
        """
        regions_set = set(labels)
        obj_val = sum(
            self.metric(attr[i].reshape(1, -1), attr[j].reshape(1, -1))
            for r in regions_set
            for i, j in itertools.combinations(np.where(labels == r)[0], 2))
        
        return float(obj_val)

    def update(self, moving_area, recipient_region, labels, attr):
        donor_region = labels[moving_area]

        attr_donor = attr[labels == donor_region]
        donor_diff = sum(
            self.metric(attr_donor, attr[moving_area].reshape(1, -1)))

        attr_recipient = attr[labels == recipient_region]
        recipient_diff = sum(
            self.metric(attr_recipient, attr[moving_area].reshape(1, -1)))
    
        return float(recipient_diff - donor_diff)

    def natural_weight(self, attr, ndist = 7):
        return self(np.zeros(attr.shape[0]), attr)/ndist
        #/ len(l1)**2 * (len(l1)/ndist)**2 * ndist ,
        #per pair       number of pairs per dist   districts
        
class ObjectiveFunctionCenter(ObjectiveFunction):
    def __init__(self, metric=None, center=np.mean, reduction=np.sum):
        """
        Parameters
        ----------
        metric : function
            Refer to the corresponding argument in
            :meth:`ObjectiveFunction.__init__`.
        center : function, default: np.mean
            Function for calculating the center of the attributes of the areas
            belonging to the same region.
        reduction : function, default: np.sum
            Function used for

            * reducing the intraregional distances to a scalar and
            * reducing these scalars of the regions to one single scalar.
        For example, the defaults make the objective function the sum over 
        regions of the sum over areas within the region of distances from the 
        mean.
        """
        self.center = center
        self.reduction = reduction
        super().__init__(metric)

    def __call__(self, labels, attr):
        """
        Examples
        --------
        >>> from sklearn.metrics.pairwise import distance_metrics
        >>> metric = distance_metrics()["manhattan"]
        >>> labels = np.array([0, 1, 1])
        >>> attr = np.array([1, 2, 2]).reshape(-1, 1)
        >>> objective = ObjectiveFunctionCenter(metric)
        >>> int(objective(labels, attr))
        0
        >>> attr = np.array([1, 2, 3]).reshape(-1, 1)
        >>> objective = ObjectiveFunctionCenter(metric)
        >>> int(objective(labels, attr))
        1
        """
        regions = sorted(set(labels))
        objective_per_region = [
            self._intraregional_heterogeneity(labels, r, attr)
            for r in regions
        ]
        obj_val = self.reduction(objective_per_region)
        return obj_val

    def _intraregional_heterogeneity(self, labels, region, attr):
        return self.reduction(
            self.metric(
                attr[labels == region],
                self.center(attr[labels == region], axis=0).reshape(1, -1)),
            axis=0)

    def update(self, moving_area, recipient_region, labels, attr):
        donor_region = labels[moving_area]

        donor_before = self._intraregional_heterogeneity(
            labels, donor_region, attr)
        recipient_before = self._intraregional_heterogeneity(
            labels, recipient_region, attr)

        labels[moving_area] = recipient_region
        donor_after = self._intraregional_heterogeneity(
            labels, donor_region, attr)
        recipient_after = self._intraregional_heterogeneity(
            labels, recipient_region, attr)
        labels[moving_area] = donor_region

        overall_before = self.reduction((donor_before, recipient_before))
        overall_after = self.reduction((donor_after, recipient_after))
        diff = overall_after - overall_before

        return diff

class ObjectiveFunctionBalance(ObjectiveFunction):
    def __call__(self, labels, attr):
        """
        Objective function that tries to reduce variation between 
        regions' total magnitudes
        """
        regions_set = set(labels)
        region_totals =[sum(attr[i] for i in np.where(labels == r)[0])
                        for r in regions_set]
        obj_val = float(max(region_totals)-min(region_totals))
        return obj_val

    def update(self, moving_area, recipient_region, labels, attr):
        old = self(labels, attr)
        comebackregion = labels[moving_area]
        labels[moving_area] = recipient_region
        new = self(labels, attr)
        labels[moving_area] = comebackregion
        return new - old

    def natural_weight(self, attr, ndist = 7):
        return float(.05*sum(attr))


class ObjectiveFunctionComposite(ObjectiveFunction):
    """Create new class that combines objective functions for several
    groups of attributes.  This accepts a list of tuples the first
    element of which another objective function and the rest of which
    are its arguments.
        
    Examples
    --------
    >>> from sklearn.metrics.pairwise import distance_metrics
    >>> metric = distance_metrics()["manhattan"]
    >>> labels = np.array([0, 0, 0, 0, 1, 1])
    >>> attr = np.arange(len(labels)).reshape(-1, 1)
    >>> objective = ObjectiveFunctionComposite([ObjectiveFunctionPairwise,
                                                ObjectiveFunctionCenter], 
                                                [(), (np.sum, )], metric)
    >>> int(objective(labels, attr))
    11
    """
    def __init__(self, funclist, attrlist,
                 weights = None, metric = None, arglist = None):
        """
        Parameters
        ----------
        funclist: list
            list of function names
        attrlist: list of attributes to be applied to each function
        weights: list
            How to weight each function.  
        metric : function
            The metric to use for all listed functions and to compose 
            the results of each function
            Refer to the metric argument in
            :meth:`ObjectiveFunction.__init__`.
        """
        if metric not in ["manhattan", None]:
            print('''code needs fixing for metrics other than "manhattan".
                     Using "manhattan."''')
            metric = None
        super().__init__(metric)
        self.weights = weights
        self.get_ranges_from_attrlist(attrlist)
        self.flat_attr_list = [i for j in attrlist for i in j]
        if arglist == None:
            arglist = [() for f in funclist]
        self.functions = [f(*a) for (f, a) in zip(funclist, arglist)]

    def get_ranges_from_attrlist(self, attrlist):
        # returns list of tuples representing ranges of each
        # sub-objective attribute.  
        self.ranges = [0]
        for it in attrlist:
            try:
                l = len(it)
            except TypeError:
                l = 1
            self.ranges.append( self.ranges[-1]+l )
        self.ranges = list(zip(self.ranges, self.ranges[1:]))

    def __call__(self, labels, attr):
        '''
        Parameters
        ----------
        labels: vector-like
            vector of areas each region belongs to
        attr: array
            array of attributes of each region, with columns in order of 
            attribute list.  
        '''
        vec = self.objvec(labels, attr)
        return self.metric(vec, 0*vec).reshape(1)

    def objvec(self, labels, attr):
        if attr.shape[1] != len(self.flat_attr_list):
            raise ValueError(
                "The attribute array has {} columns, but the total number\n"
                "of attributes listed is {}\n"
                "attr[1,:] is {}\n"
                "attribute list is {}\n"
                .format(
                    attr.shape[1],
                    len(self.flat_attr_list),
                    attr[1,:],
                    self.flat_attr_list
                )
            )
        objvec = [f(labels, attr[:,slice(*r)])
                  for (f,r) in zip(self.functions, self.ranges)]
        objvec = np.array(objvec).reshape(1,-1)
        if self.weights is not None:
            objvec *= np.array(self.weights).reshape(1,-1)
        return objvec

    def update(self, moving_area, recipient_region, labels, attr):
        # old = self.objvec(labels, attr)
        # zero = 0*old
        # ups = np.array([f.update(moving_area, recipient_region, labels,
        #                          attr[:,slice(*r)])
        #                 for (f,r)
        #                 in zip(self.functions, self.ranges)]).reshape(1,-1)
        # ups = float(self.metric(old+ups, zero)-self.metric(old,zero))

        # the above is too slow, but the following only works for
        # the manhattan metric.  
        ups = np.array(
            [f.update(moving_area, recipient_region, labels,
                      attr[:, slice(*r)])
             for (f, r)
             in zip(self.functions, self.ranges)]
            ).reshape(1,-1)
        if self.weights is not None:
            ups *= np.array(self.weights).reshape(1,-1)
                
        return float(ups.sum())

class ObjectiveFunctionCompactness(ObjectiveFunction):
    def __call__(self, labels, attr):
        """
        Objective function that tries to reduce total perimeter.  
        attr must be the geometry series
        """
        g = gpd.GeoDataFrame(attr, columns = ['geometry'])
        g['templab'] = labels
        lengths = g.dissolve(by ='templab').length
 
        return sum(lengths)

    def update(self, moving_area, recipient_region, labels, attr):
        # the boundary between the moving area and its neighbors in
        # the same region is added, and the boundary between it and
        # its neighbors in the recipient region is lost.

        g = gpd.GeoDataFrame(attr, columns = ['geometry'])
        w = (labels == moving_area).astype(int)
        w -= (labels == labels[recipient_region]).astype(int)
        w[moving_area] = 0
        lengths = [a.intersection(g.geometry[moving_area]).length * w[i]
                   for i,a in enumerate(g.geometry)]
        return sum(lengths)*2

    def natural_weight(self, attr, ndist = 7):
        return self(np.zeros(attr.shape[0]), attr) * ndist**.5
    



