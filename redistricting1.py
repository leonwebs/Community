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
    #    geojson knows how to read urls, so no need for explicit requests module
        geodat = gpd.read_file(url)
        geodat.to_file(filename + '.geojson', driver='GeoJSON')
        geodat.to_file(filename)
    else:
        geodat = gpd.read_file(filename+'.geojson')
    #convert all to numeric where possible
    geodat = geodat.apply(pd.to_numeric, errors = 'ignore')
    #'pop' is not a good name for population
    if 'pop' in geodat.columns:
        geodat.rename({'pop':'population'}, axis = 'columns', inplace = True)

    return geodat
#tractdat.plot()

files = ['tracts', 'counties', 'districts']
urls = ['https://data.colorado.gov/resource/aevh-apr2.geojson?$limit=1300',
        'https://data.colorado.gov/resource/ewkj-ipn7.geojson',
        'https://data.colorado.gov/resource/jz4n-qus2.geojson'] 

geodata = {eachfile: loaddata(eachfile, eachurl) for (eachfile, eachurl) in zip(files, urls)}


'''The datasets are missing data; the medians sometimes not defined for a
tract.  For now we won't use columns without data and later go back
and deal with nans using perhaps `DataFrame.fillna()`.  To start we'll
limit our analysis to communnities of interest defined by race and
ethnicity.  '''
print('The following columns have nan elements')
badcol = geodata['tracts'].columns[geodata['tracts'].isnull().any()]
print(list(badcol))


racecat = [ 'hispanic', 'white_nh', 'black_nh', 'ntvam_nh', 'asian_nh', 'hawpi_nh', 'other_nh', 'twoplus_nh']
#agecat = [i for i in tractdat.columns if 'age' in i and i not in badcol]
#incomecat = []
#all income categories have some nans!
#educationcat = [i for i in tractdat.columns if 'gr' in i and i not in badcol]
#educationcat.extend(['enrolled', 'n_enrolled'])

'''First we'd like to answer the question "Where are the communities?"
The `max-p` algorithm divides a set of areas into regions with similar
characteristicts.  The number of regions is not set, but is chosen by
the algorithm to optimize intra-region similarity.  It does require a
minimum value for each region, in this case we'll say that each region
requires at least 250,000 people, about 5% of the state.  '''


'''The maxp algorithm takes some time with the 1250 census tracts.  
We'll only do it if asked or if there's no prior saved file.  '''

#new_maxp = False
#
#def genmaxp(filename):
#    w = ps.queen_from_shapefile(filename+'/'+filename+'.shp', idVariable = 'geonum')  
#    z = geodata[filename][racecat].values
#
#    print("Beginning maxp regionalization ...")
#    maxp = ps.region.Maxp(w, z, 500000 , geodata[filename].population, initial=300)
#    print("... done.")
#    
#    lbls = pd.Series(maxp.area2region).reindex(geodata[filename]['geonum'].astype(str))
#    geodata[filename]= geodata[filename].assign(regindex_maxp = lbls.values)
#    
#    geodata[filename].to_file(filename+'.geojson', driver='GeoJSON')
#    
#    
#if new_maxp == True or 'regindex_maxp' not in geodata['tracts'].columns:
#    genmaxp('tracts')
#

    

'''Now we plot'''



#f, ax = plt.subplots(1, figsize=(9, 9))
#geodata['tracts'].plot(column='regindex_maxp',
#       categorical=True,
#       linewidth=0.1,
#       edgecolor='white',
#       ax=ax)
#
#ax.set_axis_off()
#plt.show()


'''Of course these cannot be congressional districts.  There must be only
7 districts, one for each seat Colorado has in the House of
Representatives.  In addition, there must be close to equal population
in each district.  

Now we will use the AZP algorithm to generate a specific number of
districts.  The algorithm optimizes an objective function, which in this
case includes intra-region similarity and total population.  '''

ndist = 7
distpop = geodata['tracts'].population.sum() / ndist 


'''The AZP algorithm also takes some time with the 1250 census tracts.  
The exact versions of these problems are np hard, and even the heuristic
takes a while.  
Again we'll only do it if asked or if there's no prior saved file.  '''

new_azp = False

def genazp(filename):
    popweightfactor=1
    geodata[filename].population = geodata[filename].population*popweightfactor
    
    pregazp = region.p_regions.azp.AZP()
    print("Beginning AZP regionalization ...")
    pregazp.fit_from_geodataframe(geodata[filename], ['population']+racecat, 
                                  ndist, contiguity = "queen", 
                                  objective_func = region.objective_function.ObjectiveFunctionPairwiseWithTotal() )
    print("... done.")
    geodata[filename].population = geodata[filename].population/popweightfactor
    
    geodata[filename]= geodata[filename].assign(regindex_azp = pregazp.labels_)
    
    geodata[filename].to_file(filename+'.geojson', driver='GeoJSON')
    
    
if new_azp == True or 'regindex_azp' not in geodata['tracts'].columns:
    genazp('tracts')


'''Plotting this we have'''

f1, ax1 = plt.subplots(1, figsize=(9,9))
geodata['tracts'].plot(column = 'regindex_azp', 
       categorical = True, 
       linewidth = .1,
       edgecolor = 'white',
       legend = True,
       ax = ax1)
ax1.set_axis_off()



regpops = [sum([geodata['tracts'].population[i] for i in np.where(geodata['tracts'].regindex_azp == j)[0]]) for j in range(7)]
print(regpops)
np.log10(np.var(regpops))


'''These districts obviously show no regard for other criteria of good 
congressional districts, like compactness, overlap with current districts 
(below) or respect for natural features like mountain ranges.  These could be 
included in the analysis by editing the objective function.  '''

'''For comparison we include Colorado's current districts'''

f2, ax2 = plt.subplots(1, figsize=(9, 9))
geodata['districts'].plot(column="emp",
       linewidth = .1, 
       categorical = True,
       edgecolor = 'white',
       ax=ax2)
ax2.set_axis_off()

#os.path.isfile('censuscounties17_lab.geojson')
#os.path.pardir
#os.getcwd()
#os.chdir('Documents\Interests\PythonLearning\Redistricting')


regpops = [sum([geodata['tracts'].population[i] for i in np.where(geodata['tracts'].regindex_azp == j)[0]]) for j in range(7)]
spanpops= [sum([geodata['tracts'].hispanic[i] for i in np.where(geodata['tracts'].regindex_azp == j)[0]]) for j in range(7)]
whitepops = [sum([geodata['tracts'].white_nh[i] for i in np.where(geodata['tracts'].regindex_azp == j)[0]]) for j in range(7)]
ntv= [sum([geodata['tracts'].ntvam_nh[i] for i in np.where(geodata['tracts'].regindex_azp == j)[0]]) for j in range(7)]

f3, ax3 = plt.subplots(1)
plt.bar(range(7),[i/(j+1) for (i,j) in zip(spanpops, regpops)])

f4, ax4 = plt.subplots(1)
plt.bar(range(7),[i/(j+1) for (i,j) in zip(ntv, regpops)])

f5, ax5 = plt.subplots(1)
plt.bar(range(7),[i/(j+1) for (i,j) in zip(whitepops, regpops)])

#lots of help from http://darribas.org/gds_scipy16/ipynb_md/07_spatial_clustering.html