# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:20:07 2019

@author: leonwebs
"""

#bring up new window for plotting
#%matplotlib qt

#import requests
import os 
import pysal as ps
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import region


def loaddata(filename, url):
    if not(os.path.isfile(filename+'.geojson')):
        print("Retrieving the data and storing to a file")
    #    req = requests.get(url, filename)
    #    tractdat = req.json()
    #    geojson knows how to read urls, so no need for requests module
        geodat = gpd.read_file(url)
        geodat.to_file(filename + '.geojson', driver='GeoJSON')
        geodat.to_file(filename)
    else:
        geodat = gpd.read_file(filename)
    #convert all to numeric where possible
    geodat = geodat.apply(pd.to_numeric, errors = 'ignore')
    #'pop' is not a good name for population
    if 'pop' in geodat.columns:
        geodat.rename({'pop':'population'}, axis = 'columns', inplace = True)

    return geodat
#tractdat.plot()
tractdat = loaddata('censustracts17','https://data.colorado.gov/resource/aevh-apr2.geojson?$limit=1300')
countydat = loaddata('censuscounties17','https://data.colorado.gov/resource/ewkj-ipn7.geojson')
currentdist = loaddata('censusdist','https://data.colorado.gov/resource/jz4n-qus2.geojson') 

#medians sometimes not defined
print('The following columns have nan elements')
badcol = tractdat.columns[tractdat.isnull().any()]
list(badcol)
#later go back and deal with nans using perhaps DataFrame.fillna()

racecat = [ 'hispanic', 'white_nh', 'black_nh', 'ntvam_nh', 'asian_nh', 'hawpi_nh', 'other_nh', 'twoplus_nh']
agecat = [i for i in tractdat.columns if 'age' in i and i not in badcol]
#incomecat = []
#all income categories have some nans!
educationcat = [i for i in tractdat.columns if 'gr' in i and i not in badcol]
educationcat.extend(['enrolled', 'n_enrolled'])

ndist = 7
distpop = tractdat.population.sum() / ndist 

# Set the seed for reproducibility
np.random.seed(1234)

reload(region)

popweightfactor=1
tractdat.population = tractdat.population*popweightfactor

pregazp = region.p_regions.azp.AZP()
print("Beginning regionalization ...")
pregazp.fit_from_geodataframe(tractdat, ['population']+racecat, 
                              ndist, contiguity = "queen", 
                              objective_func = region.objective_function.ObjectiveFunctionPairwiseWithTotal() )
print("... done.")
tractdat.population = tractdat.population/popweightfactor

f, ax = plt.subplots(1, figsize=(9,9))
ctylabeled = tractdat.assign(cl = pregazp.labels_)
ctylabeled.plot(column = 'cl', 
                categorical = True, 
                legend = True, 
                linewidth = .1, 
                edgecolor = 'white', 
                ax = ax)
ax.set_axis_off()
f.show()

regpops = [sum([ctylabeled.population[i] for i in np.where(ctylabeled.cl == j)[0]]) for j in range(7)]
print(regpops)
np.log10(np.var(regpops))

ctylabeled.to_file('censuscounties17_lab.geojson', driver='GeoJSON')



#lots of help from http://darribas.org/gds_scipy16/ipynb_md/07_spatial_clustering.html