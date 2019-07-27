# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:42:15 2019

@author: leonwebs
"""

"""Testing random regions with population constraints"""

#import requests
import os 
import pysal as ps
import numpy as np
import pandas as pd
import geopandas as gpd
#import region

import randomregion

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

w = ps.queen_from_shapefile('censuscounties17/censuscounties17.shp')
wtr = ps.queen_from_shapefile('censustracts17/censustracts17.shp')

ndist =  7
distpop = sum(countydat.population)/ndist
card = [1, 1, 2,4,8,16,32]
cd = list(np.round(np.ones(ndist)*distpop))
cd[0] = round(distpop+(distpop % 1) * 6)


#t0 = ps.region.Random_Region(list(countydat.index), ndist, cardinality = card, contiguity = w)
#t1 = randomregion.Random_Region(list(countydat.index), ndist, cardinality = card, contiguity = w)
#t2 = randomregionWtCard.Random_RegionWt(list(countydat.index), ndist, cardinality = card, contiguity = w)
#
#print([i.feasible for i in [t0,t1,t2]])
#

import randomregionWtCard1
t3 = randomregionWtCard1.Random_RegionWt(list(countydat.index), ndist, 
                                        cardinality = cd, 
                                        contiguity = w, 
                                        area_wts= countydat.population,
                                        tol = .05)
    
t4 = randomregionWtCard.Random_RegionWt(list(countydat.index), ndist, 
                                        cardinality = card, 
                                        contiguity = w, 
                                        area_wts= np.ones(64))

import time
tick = time.time()

t5 = randomregion.Random_Region(list(tractdat.index), ndist, 
                                        contiguity = wtr, 
                                        compact = True)
tock = time.time()
print((tock-tick)/60)
