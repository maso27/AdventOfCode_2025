filename = './Day08/sample.txt'
verbose = 2

import open3d as o3d
import open3d.core as o3c
import numpy as np

def distance(loc1, loc2): # distance between points
    x1 = loc1[0]
    y1 = loc1[1]
    z1 = loc1[2]
    x2 = loc2[0]
    y2 = loc2[1]
    z2 = loc2[2]

    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)  # not using **0.5
    return distance

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

locations = []
loc_tensors = []
for line in lines:
    line = line.rstrip()
    parts = line.split(',')
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    locations.append((x,y,z))
    loc_tensors.append(o3c.Tensor([x,y,z]))

locations = np.array(locations)
# print(locations)
# print(loc_tensors)

octree = o3d.geometry.Octree(max_depth=4)
octree.convert_from_point_cloud(loc_tensors)

print(o3d.geometry.KDTreeFlann(octree))

# o3d.visualization.draw_geometries([octree])

x_min, x_max = np.min(locations[:,0]), np.max(locations[:,0])
y_min, y_max = np.min(locations[:,1]), np.max(locations[:,1])
z_min, z_max = np.min(locations[:,2]), np.max(locations[:,2])
