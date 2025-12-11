import numpy as np

filename = './Day09/input.txt'
verbose = 2

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

red_tiles = []
for line in lines:
    tile_a = line.split(',')
    red_tiles.append([int(tile_a[0]),int(tile_a[1])])

red_tiles = np.array(red_tiles)

largest_area = 0
for a in range(1,len(red_tiles)):
    shifted_tiles = np.roll(red_tiles, a, axis=0) # shift the tiles by a
    tile_distances = np.fabs(red_tiles - shifted_tiles) # result is distances
    tile_distances = tile_distances + 1 # length 0 is 1 tile width, etc
    tile_areas = np.multiply(tile_distances[:,0],tile_distances[:,1])
    this_largest_area = np.max(tile_areas)
    if this_largest_area > largest_area:
        largest_area = this_largest_area

print('\nDone.')
print(f'largest possible area: {largest_area}')