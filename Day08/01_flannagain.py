filename = './Day08/input.txt'
verbose = 2

import numpy as np
import pyflann as pf # had to pip import pyflann-py3

NUM_CONNECTIONS = 1000
SEARCH_DEPTH = 500

def join_circuits(circuits):
    FOUND_DUPE = False
    simpler_circuits = []
    while len(circuits) > 0:
        IS_OVERLAP=False
        for a in range(1,len(circuits)):
            dupes = np.rec.find_duplicate(list(circuits[0]) + list(circuits[a]))
            if len(dupes) > 0:
                IS_OVERLAP = True
                FOUND_DUPE = True
                break
        if IS_OVERLAP:
            simpler_circuits.append(circuits.pop(a) | circuits.pop(0)) # combining two sets
        else:
            simpler_circuits.append(circuits.pop(0))
    return simpler_circuits, FOUND_DUPE

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

locations = []
for line in lines:
    line = line.rstrip()
    parts = line.split(',')
    x,y,z = parts
    locations.append((x,y,z))

locations = np.array(locations).astype(float)
if verbose >= 3:
    print(locations)

flann = pf.FLANN()
indices, dists = flann.nn(locations, locations, SEARCH_DEPTH, algorithm='kmeans', 
                          branching=32, iterations=7, checks=16)

indices = np.delete(indices, 0, 1) # remove first element (self-index)
dists = np.delete(dists, 0, 1)   # remove first element (self-distance)

if verbose >= 3:
    print(f'indices:\n{indices}')
    print(f'dists:\n{dists}')

# find shortest distances
shortest_indices = np.argsort(dists, axis=None) # locations of shortest distances
# skip every other index (because it's same 2 points but from the other end)
shortest_indices = np.delete(shortest_indices, np.arange(1, len(shortest_indices), 2))

if verbose >= 3:
    print(shortest_indices)

# extracting point pairs in order of shortest distance
lines_list = []
for idx in shortest_indices[:(NUM_CONNECTIONS)]:
    p1 = int(idx / (SEARCH_DEPTH - 1)) # first point is the row
    p2 = int(indices.flatten()[idx])   # second point is where the index is pointing
    lines_list.append([p1,p2])

# lines_list = np.array(lines_list)

# build circuits
circuits = [] # a list of sets
for p1,p2 in lines_list:
    IN_CIRCUIT = False
    for a, circuit in enumerate(circuits):
        if (p1 in circuit) or (p2 in circuit):
            IN_CIRCUIT = True
            circuits[a].add(p1)
            circuits[a].add(p2) # += [p1, p2]
            break
    if not IN_CIRCUIT:
        circuits.append({p1,p2})
if verbose >= 3:
    print(f'all circuits:\n{circuits}')

# join all fractured circuits
KEEP_GOING = True
while KEEP_GOING:
    circuits, KEEP_GOING = join_circuits(circuits)

if verbose >= 3:
    print(f'joined circuits:\n{circuits}')

# establish circuit lengths to sort
circuit_lengths = []
for circuit in circuits:
    circuit_lengths.append(len(circuit))
circuit_lengths.sort(reverse=True)
if verbose >= 2:
    print(f'\nlengths of top 10 circuits, sorted: {circuit_lengths[:10]}')

print('\nDone.')
print(f'lengths of 3 longest circuits multiplied: {circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]}')