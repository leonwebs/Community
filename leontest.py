import clusterpy
import shapefile as shp  # Requires the pyshp package
import matplotlib.pyplot as plt


calif = clusterpy.importArcData("clusterpy/data_examples/CA_Polygons")
print("step 1")
calif.cluster('arisel', ['PCR2002'], 9, wType = 'rook', inits = 10, dissolve = 1)
print("step 2")
calif.results[0].exportArcData("leontest")
print("step 3")
sf = shp.Reader("leontest.shp")

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()
