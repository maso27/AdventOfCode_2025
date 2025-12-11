filename = './Day08/sample.txt'
verbose = 2

import numpy as np
import pyflann as pf # had to pip import pyflann-py3d

NUM_CONNECTIONS = 10
SEARCH_DEPTH = 5


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
print(locations)

flann = pf.FLANN()
indices, dists = flann.nn(locations, locations, SEARCH_DEPTH, algorithm='kmeans', 
                          branching=32, iterations=7, checks=16)

indices = np.delete(indices, 0, 1) # remove first element (self-index)
dists = np.delete(dists, 0, 1)   # remove first element (self-distance)

print(f'indices:\n{indices}')
print(f'dists:\n{dists}')

# find shortest distances
shortest_indices = np.argsort(dists, axis=None) # locations of shortest distances
# skip every other index (because it's same 2 points but from the other end)
shortest_indices = np.delete(shortest_indices, np.arange(1, len(shortest_indices), 2))

print(shortest_indices)

# extracting point pairs in order of shortest distance
lines_list = []
for idx in shortest_indices[:(NUM_CONNECTIONS)]:
    p1 = int(idx / (SEARCH_DEPTH - 1)) # first point is the row
    p2 = int(indices.flatten()[idx])   # second point is where the index is pointing
    lines_list.append([p1,p2])

# lines_list = np.array(lines_list)

# build circuits
circuits = []
for p1,p2 in lines_list:
    IN_CIRCUIT = False
    for a, circuit in enumerate(circuits):
        if (p1 in circuit) or (p2 in circuit):
            IN_CIRCUIT = True
            circuits[a] += [p1, p2]
            break
    if not IN_CIRCUIT:
        circuits.append([p1,p2])
print(f'all circuits:\n{circuits}')

# TODO: join circuits that need it
# join_done = False
# while not join_done:
#     circuits, join_done = join_circuits(circuits)

iterations = 0
for a, this_circuit in enumerate(circuits):
    IS_OVERLAP = False
    for b, that_circuit in enumerate(circuits):
        if a == b:
            continue
        for this_item in this_circuit:
            if this_item in that_circuit:
                IS_OVERLAP = True
                break
        


# remove duplicates within circuits
less_circuits = []
for circuit in circuits:
    dupes = [0]
    while(len(dupes) > 0):
        dupes = np.rec.find_duplicate(np.array(circuit))
        for dupe in dupes:
            circuit.remove(dupe)
    less_circuits.append(circuit)

print(f'resulting circuits:\n{less_circuits}')