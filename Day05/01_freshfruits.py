filename = './Day05/input.txt'
verbose = 3

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

is_ranges = True
ranges = set()
ingredients = set()
for line in lines:
    if line.rstrip() == '':
        is_ranges = False
        continue
    if is_ranges:
        parts = line.rstrip().split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.add((start,end))
    else:
        ingredient = int(line.rstrip())
        ingredients.add(ingredient)

fresh_ones = 0
for ingredient in ingredients:
    for region in ranges: # calling it region to avoid breaking "range"
        if ingredient >= region[0] and ingredient <= region[1]:
            if verbose >= 2:
                print(f'ingredient {ingredient} is fresh')
            fresh_ones += 1
            break

print('Done.')
print(f'  Number of fresh ingredients: {fresh_ones}')