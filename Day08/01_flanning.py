filename = './Day08/sample.txt'
verbose = 2

import pyflann as pf
import numpy as np

# def distance(loc1, loc2): # distance between points
#     x1 = loc1[0]
#     y1 = loc1[1]
#     z1 = loc1[2]
#     x2 = loc2[0]
#     y2 = loc2[1]
#     z2 = loc2[2]

#     distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)  # not using **0.5
#     return distance

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

locations = []
for line in lines:
    line = line.rstrip()
    parts = line.split(',')
    x = float(parts[0])
    y = float(parts[1])
    z = float(parts[2])
    locations.append((x,y,z))

locations = np.array(locations)

print (locations)
flann = pf.FLANN()
result, dists = flann.nn(locations, locations, 5, algorithm='kmeans', branching=32, iterations=7, checks=16)


print("Indices of Nearest Neighbors:\n", result)
print("Distances to Nearest Neighbors:\n", dists)

# x_min, x_max = np.min(locations[:,0]), np.max(locations[:,0])
# y_min, y_max = np.min(locations[:,1]), np.max(locations[:,1])
# z_min, z_max = np.min(locations[:,2]), np.max(locations[:,2])
