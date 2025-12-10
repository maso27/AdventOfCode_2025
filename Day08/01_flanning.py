filename = './Day08/sample.txt'
verbose = 2

import pyflann as pf # had to pip import pyflann-py3d
import numpy as np

SEARCH_DEPTH = 5

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

if verbose >= 4:
    print (locations)
flann = pf.FLANN()
result, dists = flann.nn(locations, locations, SEARCH_DEPTH, algorithm='kmeans', branching=32, iterations=7, checks=16)

result = np.delete(result, 0, 1) # remove first element (self-index)
dists = np.delete(dists, 0, 1)   # remove first element (self-distance)

if verbose >= 2:
    print("Indices of Nearest Neighbors:\n", result)
    print("Distances to Nearest Neighbors:\n", dists)

# find shortest distances
shortest_indexes = np.argsort(dists, axis=None)
# skip every other index (because it's same 2 points from the other end)
shortest_indexes = np.delete(shortest_indexes, np.arange(1, len(shortest_indexes), 2))

if verbose >= 3:
    print(f'shortest distances: {shortest_indexes}')

for idx in shortest_indexes[:10]:
    point1 = int(idx / (SEARCH_DEPTH - 1)) # first point is the row
    point2 = result.flatten()[idx]         # second point is where the index is pointing
    if verbose >= 2:
        print(f'Point {point1} is distance: {dists.flatten()[idx]} from point {point2}')
    if verbose >= 1:
        print(f'  {locations[point1]} to {locations[point2]}')

  
