filename = './Day08/sample.txt'
verbose = 2

# import numpy as np

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

def distance(loc1, loc2): # distance between points
    x1 = loc1[0]
    y1 = loc1[1]
    z1 = loc1[2]
    x2 = loc2[0]
    y2 = loc2[1]
    z2 = loc2[2]

    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
    return distance