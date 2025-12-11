import numpy as np

filename = './Day09/sample.txt'
verbose = 3

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

def check_dir(this_tile, next_tile, last_dir):
    IS_LEFT = False
    if next_tile[0] == this_tile[0]:    # vertical move
        if next_tile[1] > this_tile[1]: # move up
            dir = '^'
            if last_dir == '>':
                IS_LEFT = True
        else:                           # move down
            dir = 'v'
            if last_dir == '<':
                IS_LEFT = True
    else:                               # horizontal move
        if next_tile[0] > this_tile[0]: # move right
            dir = '>'
            if last_dir == 'v':
                IS_LEFT = True
        else:                           # move left
            dir = '<'
            if last_dir == '^':
                IS_LEFT = True
    return dir, IS_LEFT

def findgreens(red_tiles):
    this_tile = red_tiles.pop(0)
    red_tiles.append(this_tile) # stick it on the end
    direction,_ = check_dir(this_tile, red_tiles[0], '')
    num_lt = 0
    num_rt = 0
    while len(red_tiles) > 0:
        next_tile = red_tiles.pop(0)
        direction, was_left = check_dir(this_tile, next_tile, direction)
        if was_left:
            num_lt += 1
        else:
            num_rt += 1
        if verbose >= 3:
            turn = 'left' if was_left else 'right'
            print(f'from {this_tile} to {next_tile}: direction is {direction}, {turn}')
        this_tile = next_tile
    if num_rt > num_lt:
        clockwise = True
    else:
        clockwise = False
    if verbose >= 2:
        rotation = 'clockwise' if clockwise else 'counter-clockwise'
        print(f'made {num_lt} lefts and {num_rt} rights. Rotation is {rotation}')
    # TODO: fill greens
    

red_tiles = []
for line in lines:
    tile_a = line.split(',')
    red_tiles.append([int(tile_a[0]),int(tile_a[1])])

# red_tiles = np.array(red_tiles)

# TODO: step through tiles and mark green connector tiles
# TODO: count left and right turns to determine inside
findgreens(red_tiles)
# TODO: mark insides as green

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