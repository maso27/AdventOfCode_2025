filename = './Day07/input.txt'
verbose = 0

# import numpy as np

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

# find S
line = lines[0]
s_loc = (line.find('S'),0)
if verbose >= 3:
    print(f'Start location: {s_loc}')

# find splitters
splitters = []
for a, line in enumerate(lines):
    found = 0 # intializing not -1
    while found >= 0:
        new_found = line[found:].find('^')
        if new_found == -1:
            break
        splitters.append((found + new_found, a))
        found += new_found + 1 # iterating to the next position
if verbose >= 3:
    print(f'Splitters found at locations: {splitters}')

# find valid splits
valid_splits = 0
valid_splitters = []
this_line = [s_loc[0]]
for a in range(len(lines)):
    for location in this_line.copy():
        if (location,a) in splitters:
            this_line.remove(location)
            if (location-1) not in this_line:
                this_line.append((location-1))
            if (location+1) not in this_line:
                this_line.append((location+1))
            valid_splits += 1
            valid_splitters.append((location,a))
            if verbose >= 2:
                print(f'Valid split at line {a} for location {(location,a)}')

if verbose >= 2:
    print(f'Valid splitters: {valid_splitters}')
print(f'Total valid splits: {valid_splits}')

# find valid realities
realities = 1
this_line = [s_loc[0]]
for a in range(len(lines)):
    for location in this_line.copy():
        if (location,a) in splitters:
            this_line.remove(location)
            this_line.append((location-1))
            this_line.append((location+1))
            realities += 1
            if verbose >= 2:
                print(f'Valid split at line {a} for location {(location,a)}')
print(f'Total valid realities: {realities}')