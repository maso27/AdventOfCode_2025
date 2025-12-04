filename = './Day04/input.txt'
verbose = 2

def removable_rolls(roll_spots):
    # find number of adjacents
    valid_rolls = set()
    for spot in roll_spots:
        adjacent_rolls = 0
        if (spot[0]-1,spot[1]-1) in roll_spots:
            adjacent_rolls += 1
        if (spot[0]-1,spot[1]) in roll_spots:
            adjacent_rolls += 1
        if (spot[0]-1,spot[1]+1) in roll_spots:
            adjacent_rolls += 1
        if (spot[0],spot[1]-1) in roll_spots:
            adjacent_rolls += 1
        if (spot[0],spot[1]+1) in roll_spots:
            adjacent_rolls += 1
        if (spot[0]+1,spot[1]-1) in roll_spots:
            adjacent_rolls += 1
        if (spot[0]+1,spot[1]) in roll_spots:
            adjacent_rolls += 1
        if (spot[0]+1,spot[1]+1) in roll_spots:
            adjacent_rolls += 1
        if adjacent_rolls < 4:
            if verbose >= 3:
                print(f'adding {spot} to removable rolls')
            valid_rolls.add(spot)
    return valid_rolls

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

# catalog roll locations
roll_spots = set()
for row_num, line in enumerate(lines):
    line = line.rstrip()
    for col_num, spot in enumerate(line):
        if spot == '@':
            roll_spots.add((col_num, row_num))

if verbose >= 3:
    print(f'Roll locations: {roll_spots}')

rolls_removed = removable_rolls(roll_spots)
rolls_remaining = roll_spots.difference(rolls_removed)
if verbose >= 3:
    print(f'rolls remaining: {rolls_remaining}')

while len(rolls_removed) > 0:
    rolls_removed = removable_rolls(rolls_remaining)
    rolls_remaining = rolls_remaining.difference(rolls_removed)
    print(f'rolls remaining: {rolls_remaining}')

if verbose >= 2:
    print(f':Total rolls removed {roll_spots.difference(rolls_remaining)}')

print('Done.')
print(f'  Number of valid rolls: {len(roll_spots) - len(rolls_remaining)}')