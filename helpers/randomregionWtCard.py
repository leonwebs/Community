# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:13:36 2019

@author: leonwebs
"""

"""
Generate random regions

Randomly form regions given various types of constraints on cardinality and
composition.

This is edited from pysal.region.randomregion to allow weighted cardinality.
For example, total population in each region can be constrained rather than the 
number of areas.  
"""

__author__ = "David Folch dfolch@fsu.edu, Serge Rey srey@asu.edu"

import numpy as np
from pysal.region.components import check_contiguity
from pysal.common import copy

__all__ = ["Random_RegionsWt", "Random_RegionWt"]


class Random_RegionsWt:
    """Generate a list of Random_Region instances.

    Parameters
    ----------

    area_ids        : list
                      IDs indexing the areas to be grouped into regions (must
                      be in the same order as spatial weights matrix if this
                      is provided)

    num_regions     : integer
                      number of regions to generate (if None then this is
                      chosen randomly from 2 to n where n is the number of
                      areas)

    cardinality     : list
                      list containing the number of areas to assign to regions
                      (if num_regions is also provided then len(cardinality)
                      must equal num_regions; if cardinality=None then a list
                      of length num_regions will be generated randomly)

    contiguity      : W
                      spatial weights object (if None then contiguity will be
                      ignored)

    maxiter         : int
                      maximum number attempts (for each permutation) at finding
                      a feasible solution (only affects contiguity constrained
                      regions)

    compact         : boolean
                      attempt to build compact regions, note (only affects
                      contiguity constrained regions)

    max_swaps       : int
                      maximum number of swaps to find a feasible solution
                      (only affects contiguity constrained regions)

    permutations    : int
                      number of Random_Region instances to generate

    Attributes
    ----------

    solutions       : list
                      list of length permutations containing all Random_Region instances generated

    solutions_feas  : list
                      list of the Random_Region instances that resulted in feasible solutions

    Examples
    --------

    Setup the data

    >>> import random
    >>> import numpy as np
    >>> import pysal
    >>> nregs = 13
    >>> cards = range(2,14) + [10]
    >>> w = pysal.lat2W(10,10,rook=True)
    >>> ids = w.id_order

    Unconstrained

    >>> random.seed(10)
    >>> np.random.seed(10)
    >>> t0 = pysal.region.Random_Regions(ids, permutations=2)
    >>> t0.solutions[0].regions[0]
    [19, 14, 43, 37, 66, 3, 79, 41, 38, 68, 2, 1, 60]

    Cardinality and contiguity constrained (num_regions implied)

    >>> random.seed(60)
    >>> np.random.seed(60)
    >>> t1 = pysal.region.Random_Regions(ids, num_regions=nregs, cardinality=cards, contiguity=w, permutations=2)
    >>> t1.solutions[0].regions[0]
    [62, 61, 81, 71, 64, 90, 72, 51, 80, 63, 50, 73, 52]

    Cardinality constrained (num_regions implied)

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t2 = pysal.region.Random_Regions(ids, num_regions=nregs, cardinality=cards, permutations=2)
    >>> t2.solutions[0].regions[0]
    [37, 62]

    Number of regions and contiguity constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t3 = pysal.region.Random_Regions(ids, num_regions=nregs, contiguity=w, permutations=2)
    >>> t3.solutions[0].regions[1]
    [62, 52, 51, 63, 61, 73, 41, 53, 60, 83, 42, 31, 32]

    Cardinality and contiguity constrained

    >>> random.seed(60)
    >>> np.random.seed(60)
    >>> t4 = pysal.region.Random_Regions(ids, cardinality=cards, contiguity=w, permutations=2)
    >>> t4.solutions[0].regions[0]
    [62, 61, 81, 71, 64, 90, 72, 51, 80, 63, 50, 73, 52]

    Number of regions constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t5 = pysal.region.Random_Regions(ids, num_regions=nregs, permutations=2)
    >>> t5.solutions[0].regions[0]
    [37, 62, 26, 41, 35, 25, 36]

    Cardinality constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t6 = pysal.region.Random_Regions(ids, cardinality=cards, permutations=2)
    >>> t6.solutions[0].regions[0]
    [37, 62]

    Contiguity constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t7 = pysal.region.Random_Regions(ids, contiguity=w, permutations=2)
    >>> t7.solutions[0].regions[1]
    [62, 61, 71, 63]

    """
    def __init__(
        self, area_ids, num_regions=None, cardinality=None, contiguity=None,
        maxiter=100, compact=False, max_swaps=1000000, permutations=99, 
        area_wts=None, tol = 0):

        solutions = []
        for i in range(permutations):
            solutions.append(Random_RegionWt(area_ids, num_regions, cardinality,
                                           contiguity, maxiter, compact, 
                                           max_swaps, area_wts, tol))
        self.solutions = solutions
        self.solutions_feas = []
        for i in solutions:
            if i.feasible == True:
                self.solutions_feas.append(i)


class Random_RegionWt:
    """Randomly combine a given set of areas into two or more regions based
    on various constraints.


    Parameters
    ----------

    area_ids        : list
                      IDs indexing the areas to be grouped into regions (must
                      be in the same order as spatial weights matrix if this
                      is provided)
                     
    area_wts        : list
                      weight to use for each area, for instance the population
                      of the area

    num_regions     : integer
                      number of regions to generate (if None then this is
                      chosen randomly from 2 to n where n is the number of
                      areas)

    cardinality     : list
                      list containing the number of areas to assign to regions
                      (if num_regions is also provided then len(cardinality)
                      must equal num_regions; if cardinality=None then a list
                      of length num_regions will be generated randomly)

    contiguity      : W
                      spatial weights object (if None then contiguity will be
                      ignored)

    maxiter         : int
                      maximum number attempts at finding a feasible solution
                      (only affects contiguity constrained regions)

    compact         : boolean
                      attempt to build compact regions (only affects
                      contiguity constrained regions)

    max_swaps       : int
                      maximum number of swaps to find a feasible solution
                      (only affects contiguity constrained regions)

    Attributes
    ----------

    feasible        : boolean
                      if True then solution was found

    regions         : list
                      list of lists of regions (each list has the ids of areas
                      in that region)

    Examples
    --------

    Setup the data

    >>> import random
    >>> import numpy as np
    >>> import pysal
    >>> nregs = 13
    >>> cards = range(2,14) + [10]
    >>> w = pysal.weights.lat2W(10,10,rook=True)
    >>> ids = w.id_order

    Unconstrained

    >>> random.seed(10)
    >>> np.random.seed(10)
    >>> t0 = pysal.region.Random_Region(ids)
    >>> t0.regions[0]
    [19, 14, 43, 37, 66, 3, 79, 41, 38, 68, 2, 1, 60]

    Cardinality and contiguity constrained (num_regions implied)

    >>> random.seed(60)
    >>> np.random.seed(60)
    >>> t1 = pysal.region.Random_Region(ids, num_regions=nregs, cardinality=cards, contiguity=w)
    >>> t1.regions[0]
    [62, 61, 81, 71, 64, 90, 72, 51, 80, 63, 50, 73, 52]

    Cardinality constrained (num_regions implied)

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t2 = pysal.region.Random_Region(ids, num_regions=nregs, cardinality=cards)
    >>> t2.regions[0]
    [37, 62]

    Number of regions and contiguity constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t3 = pysal.region.Random_Region(ids, num_regions=nregs, contiguity=w)
    >>> t3.regions[1]
    [62, 52, 51, 63, 61, 73, 41, 53, 60, 83, 42, 31, 32]

    Cardinality and contiguity constrained

    >>> random.seed(60)
    >>> np.random.seed(60)
    >>> t4 = pysal.region.Random_Region(ids, cardinality=cards, contiguity=w)
    >>> t4.regions[0]
    [62, 61, 81, 71, 64, 90, 72, 51, 80, 63, 50, 73, 52]

    Number of regions constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t5 = pysal.region.Random_Region(ids, num_regions=nregs)
    >>> t5.regions[0]
    [37, 62, 26, 41, 35, 25, 36]

    Cardinality constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t6 = pysal.region.Random_Region(ids, cardinality=cards)
    >>> t6.regions[0]
    [37, 62]

    Contiguity constrained

    >>> random.seed(100)
    >>> np.random.seed(100)
    >>> t7 = pysal.region.Random_Region(ids, contiguity=w)
    >>> t7.regions[0]
    [37, 36, 38, 39]

    """
    def __init__(
        self, area_ids, num_regions=None, cardinality=None, contiguity=None,
                    maxiter=1000, compact=False, max_swaps=1000000, 
                    area_wts=None, tol = 0):

        if area_wts is None:
            area_wts = np.ones(len(area_ids))
        self.n = sum(area_wts)
        ids = copy.copy(area_ids)
        self.wtdict = dict(zip(ids, area_wts))
        self.ids = list(np.random.permutation(ids))
        self.area_ids = area_ids
        self.regions = []
        self.feasible = True
        self.tol = tol
        self.cd_dev = {} #dictionary of deviations from intended cardinality

        # tests for input argument consistency
        if cardinality is not None:
#            if self.n != sum(cardinality):
            if np.greater_equal(abs(self.n-sum(cardinality)), .001 * abs(sum(cardinality))):
                self.feasible = False
                raise Exception('Sum of cardinalities does not equal total weight')
        if contiguity is not None:
            if area_ids != contiguity.id_order:
                self.feasible = False
                raise Exception('order of area_ids must match order in contiguity')
        if num_regions and cardinality is not None:
            if num_regions != len(cardinality):
                self.feasible = False
                raise Exception('number of regions does not match cardinality')

        # dispatches the appropriate algorithm
        if num_regions and cardinality is not None and contiguity is not None:
            # conditioning on cardinality and contiguity (number of regions implied)
            self.build_contig_regions(num_regions, cardinality, contiguity,
                                      maxiter, compact, max_swaps)
        elif num_regions and cardinality is not None:
            # conditioning on cardinality (number of regions implied)
            region_breaks = self.cards2breaks(cardinality)
            self.build_noncontig_regions(num_regions, region_breaks)
        elif num_regions and contiguity is not None:
            # conditioning on number of regions and contiguity
            cards = self.get_cards(num_regions)
            self.build_contig_regions(num_regions, cards, contiguity,
                                      maxiter, compact, max_swaps)
        elif cardinality is not None and contiguity is not None:
            # conditioning on cardinality and contiguity
            num_regions = len(cardinality)
            self.build_contig_regions(num_regions, cardinality, contiguity,
                                      maxiter, compact, max_swaps)
        elif num_regions:
            # conditioning on number of regions only
            region_breaks = self.get_region_breaks(num_regions)
            self.build_noncontig_regions(num_regions, region_breaks)
        elif cardinality is not None:
            # conditioning on number of cardinality only
            num_regions = len(cardinality)
            region_breaks = self.cards2breaks(cardinality)
            self.build_noncontig_regions(num_regions, region_breaks)
        elif contiguity is not None:
            # conditioning on number of contiguity only
            num_regions = self.get_num_regions()
            cards = self.get_cards(num_regions)
            self.build_contig_regions(num_regions, cards, contiguity,
                                      maxiter, compact, max_swaps)
        else:
            # unconditioned
            num_regions = self.get_num_regions()
            region_breaks = self.get_region_breaks(num_regions)
            self.build_noncontig_regions(num_regions, region_breaks)
            
    def get_num_regions(self):
        return np.random.random_integers(2, self.n)

    def get_region_breaks(self, num_regions):
        region_breaks = set([])
        while len(region_breaks) < num_regions - 1:
            region_breaks.add(np.random.random_integers(1, self.n - 1))
        region_breaks = list(region_breaks)
        region_breaks.sort()
        return region_breaks

    def get_cards(self, num_regions):
        region_breaks = self.get_region_breaks(num_regions)
        cards = []
        start = 0
        for i in region_breaks:
            cards.append(i - start)
            start = i
        cards.append(self.n - start)
        return cards

    def cards2breaks(self, cards):
        region_breaks = []
        break_point = 0
        for i in cards:
            break_point += i
            region_breaks.append(break_point)
        region_breaks.pop()
        return region_breaks

    def build_noncontig_regions(self, num_regions, region_breaks):
        start = 0
        for i in region_breaks:
            self.regions.append(self.ids[start:i])
            start = i
        self.regions.append(self.ids[start:])

    def grow_compact(self, w, test_card, region, candidates, potential, regpop):
        # try to build a compact region by exhausting all existing
        # potential areas before adding new potential areas
        add_areas = []
        sizecheck = self.region_size_check
        while potential and sizecheck(regpop,test_card) == -1:
            pot_index = np.random.random_integers(0, len(potential) - 1)
            add_area = potential[pot_index]
            region.append(add_area)
            regpop += self.wtdict[add_area]
            candidates.remove(add_area)
            potential.remove(add_area)
            add_areas.append(add_area)
        for i in add_areas:
            potential.extend([j for j in w.neighbors[i]
                                 if j not in region and
                                    j not in potential and
                                    j in candidates and 
                                    self.region_size_check(regpop + self.wtdict[i] , test_card)!=1])
        #regpop = sum(self.wtdict[i] for i in region)
        return region, candidates, potential, regpop

    def grow_free(self, w, test_card, region, candidates, potential, regpop):
        # increment potential areas after each new area is
        # added to the region (faster than the grow_compact)
        pot_index = np.random.random_integers(0, len(potential) - 1)
        add_area = potential[pot_index]
        tst =[self.wtdict[i]+regpop-test_card for i in w.neighbors[add_area] if i not in region and
         i not in potential and
         i in candidates and
         self.region_size_check(regpop + self.wtdict[i] , test_card)!=1]
        if any([i>0 for i in tst]):
            print(tst)
        region.append(add_area)
        regpop += self.wtdict[add_area]
        candidates.remove(add_area)
        potential.remove(add_area)
        potential.extend([i for i in w.neighbors[add_area]
                             if i not in region and
                                i not in potential and
                                i in candidates and
                                self.region_size_check(regpop + self.wtdict[i] , test_card)!=1
                                ])
        return region, candidates, potential, regpop
    
    def region_size_check(self, regsize, testsize):
        diff = regsize - testsize
        if diff > self.tol * testsize:
            return 1
        elif diff < -self.tol * testsize:
            return -1
        else:
            return 0

    def build_contig_regions(self, num_regions, cardinality, w,
                                maxiter, compact, max_swaps):
        if compact:
            grow_region = self.grow_compact
        else:
            grow_region = self.grow_free
        sizecheck = self.region_size_check
        iter = 0
        while iter < maxiter:

            # regionalization setup
            regions = []
            size_pre = 0
            counter = -1
            area2region = {}
            self.feasible = False
            swap_count = 0
            cards = copy.copy(cardinality)
            cards.sort()  # try to build largest regions first (pop from end of list)
            candidates = copy.copy(self.ids)  # these are already shuffled

            # begin building regions
            while candidates and swap_count < max_swaps:
                # setup test to determine if swapping is needed
#                print(counter, size_pre)
                if size_pre == len(regions):
                    counter += 1
                else:
                    counter = 0
                    size_pre = len(regions)
                # test if swapping is needed
#                if counter == len(candidates):
#                    
#                    # start swapping
#                    # swapping simply changes the candidate list
#                    swap_in = None   # area to become new candidate
#                    while swap_in is None:  # PEP8 E711
#                        swap_count += 1
#                        swap_out = candidates.pop(0)  # area to remove from candidates
#                        swap_neighs = copy.copy(w.neighbors[swap_out])
#                        swap_neighs = list(np.random.permutation(swap_neighs))
#                        # select area to add to candidates (i.e. remove from an existing region)
#                        for i in swap_neighs:
#                            if i not in candidates:
#                                join = i  # area linking swap_in to swap_out
#                                swap_index = area2region[join]
#                                swap_region = regions[swap_index]
#                                print("before swap: ")
#                                print([self.cd_dev[j][0]-sum([self.wtdict[i] for i in swap_region]) for j in range(len(regions))])
#                                swap_region = list(np.random.permutation(swap_region))
#                                swap_dev = self.cd_dev[swap_index]
#                                for j in swap_region:
#                                    # test to ensure region connectivity after removing area
#                                    # j is an element in the region possibly to remove
#                                    swap_region_test = swap_region[:] + [swap_out]
#                                    delta = self.wtdict[swap_out]-self.wtdict[j]
#                                    if (check_contiguity(w, swap_region_test, j) 
#                                    and sizecheck(swap_dev[0] + delta, swap_dev[0]-swap_dev[1]) == 0):
#                                        swap_in = j
#                                        break
#                            if swap_in is not None:  # PEP8 E711
#                                break
#                            else:
#                                candidates.append(swap_out)
#                    # swapping cleanup
#                    regions[swap_index].remove(swap_in)
#                    regions[swap_index].append(swap_out)
#                    area2region.pop(swap_in)
#                    area2region[swap_out] = swap_index
#                    self.cd_dev[swap_index] = tuple(i + delta for i in self.cd_dev[swap_index] )
#                    candidates.append(swap_in)
#                    counter = 0
#                    
                # setup to build a single region
                building = True
                seed = candidates.pop(0)
                region = [seed]
                regpop = self.wtdict[seed]
                if not cards:
                    print(len(regions))
                    print(sum(list(map(len,regions))))
                    print("Ran out of cards")
                    break
                test_card = cards.pop()
                #test_card is the population target;
                potential = [i for i in w.neighbors[seed] if (i in candidates
                             and sizecheck(regpop+self.wtdict[i],test_card) != 1)]
                
                # begin building single region
                while building and sizecheck(regpop, test_card)==-1:
                    if potential:
                        region, candidates, potential, regpop = grow_region(
                            w, test_card,
                                        region, candidates, potential, regpop)
                    else:
                        # not enough potential neighbors to reach test_card size
                        building = False
                        cards.append(test_card)
                        if regpop in cards:
                            # constructed region matches another candidate region size
                            cards.remove(regpop)
                        else:
                            # constructed region doesn't match a candidate region size
                            candidates.extend(region)
                            region = []
                    

                # cleanup when successful region built
                if region:
                    region_index = len(regions)
                    for i in region:
                        area2region[i] = region_index   # area2region needed for swapping

                    regions.append(region) #append the successful region to the region list
                    self.cd_dev[region_index] = np.array([regpop, regpop - test_card])
                    #print(self.cd_dev)
#                    print(building)
                    print(regpop)
#                    print(#[round(self.wtdict[i]/776646,2) for i in region],
#                           round(sum([self.wtdict[i] for i in region])/self.n*7,2))
#                    print(regpop/self.n*7)
#                    print(sum([self.wtdict[i] for i in candidates]))
#                    print(sum([len(i) for i in regions]))
#                    print(sum([sum(self.wtdict[j] for j in i) for i in regions]))
#                    print([self.cd_dev[j][0] for j in range(len(regions))])
#                    print([sum([self.wtdict[i] for i in regions[j]]) for j in range(len(regions))]) 
                    
            # handling of regionalization result
            if len(regions) < num_regions:
                # regionalization failed
                print("fail")
                self.ids = list(np.random.permutation(self.ids))
                regions = []
                iter += 1
            else:
                # regionalization successful
                self.feasible = True
                iter = maxiter
        self.regions = regions

class RegStruct(dict):
    
    def __init__(self, areas, region_list = [], area_wts = None):
        dict.__init__({area: None for area in areas})
        self.regions = [i.copy() for i in region_list]
        self.update({ area: regionind  for regionind in range(len(region_list)) for area in region_list[regionind] })
        if area_wts is None:
            self.totalfun = len #total fun accepts a list of areas and gets total weight
            self.wtfun = lambda x: 1
        else:
            self.wtdict = dict(zip(areas, area_wts))
            self.totalfun = lambda x: sum([self.wtdict[i] for i in x])
            self.wtfun = self.wtdict.get
        self.regionwts = [self.totalfun(i) for i in region_list]
            
    def area_into_region(self, area, regionind):
        if regionind == len(self.regions):
            self.regions.append([])
            self.regionwts.append(0)
        if type(area) is int:
            area = [area]
        for a in area:
            if a in self.keys():
                #remove from old region
                if self[a] is not None:
                    self.regions[self[a]].remove(a)
                    self.regionwts[self[a]] -= self.wtfun(a)
            #include in new region
            self[a] = regionind
            self.regions[regionind].append(a)
            self.regionwts[regionind] += self.wtfun(a)
    
                    