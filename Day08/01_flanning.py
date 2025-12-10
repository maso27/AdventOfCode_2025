filename = './Day08/input.txt'
verbose = 1

import pyflann as pf # had to pip import pyflann-py3d
import numpy as np

NUM_CONNECTIONS = 1000
SEARCH_DEPTH = 100;

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

locations = []
for line in lines:
    line = line.rstrip()
    parts = line.split(',')
    x,y,z = float(parts[0]), float(parts[1]), float(parts[2])
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
if verbose >= 1:
    print(f'length of the list of shortest distances: {len(shortest_indexes)}')

# figure out points based on index
lines_list = []
for idx in shortest_indexes[:NUM_CONNECTIONS]:
    point1 = int(idx / (SEARCH_DEPTH - 1)) # first point is the row
    point2 = result.flatten()[idx]         # second point is where the index is pointing
    if verbose >= 3:
        print(f'Point {point1} is distance: {dists.flatten()[idx]} from point {point2}')
    if verbose >= 2:
        print(f'  {locations[point1]} to {locations[point2]}')
    lines_list.append([point1,point2])

lines_list = np.array(lines_list)
# build circuits
circuits = []

for a in range(len(locations)):
    this_circuit = []
    a_spots = np.where(lines_list == a)
    a_spots = np.array(a_spots).T # output is row then column of locations
    if a_spots.size == 0: # empty, move to next one
        continue
    if verbose >= 3:
        print(f'location {a}')
        # print(a_spots)
    this_circuit.append(a)
    for spot in a_spots:
        other_spot = (spot[1] + 1) % 2 # toggle 1 or 0
        this_circuit.append(int(lines_list[spot[0],other_spot]))
    dupe_found = False
    for b, that_circuit in enumerate(circuits.copy()):
        dupes = np.rec.find_duplicate(np.array(this_circuit+that_circuit))
        if len(dupes) > 0: # found at least one duplicate
            for dupe in dupes:
                this_circuit.remove(dupe)
            circuits[b]+= this_circuit
            dupe_found = True
            continue
    if dupe_found == False:
        circuits.append(this_circuit)

if verbose >= 2:
    print(f'resulting circuits: {circuits}')

# establish circuit lengths to sort
circuit_lengths = []
for circuit in circuits:
    circuit_lengths.append(len(circuit))
circuit_lengths.sort(reverse=True)
if verbose >= 2:
    print(f'\nlengths of top 10 circuits, sorted: {circuit_lengths[:10]}')

print('\nDone.')
print(f'lengths of 3 longest circuits multiplied: {circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]}')

# 30492 is too low