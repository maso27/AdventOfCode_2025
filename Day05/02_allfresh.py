filename = './Day05/input.txt'
verbose = 2

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

def merge_ranges(ranges):
    merges = 0
    ranges_return = []

    ranges.sort(key=lambda x: x[0]) # sort by start value
    a = 0
    while a < len(ranges)-1:
        if ranges[a][1] >= ranges[a+1][0]: # overlap
            merges += 1
            if ranges[a][1] < ranges[a+1][1]: # make sure second end value is higher than first end value
                ranges_return.append([ranges[a][0], ranges[a+1][1]])
            else:
                ranges_return.append([ranges[a][0], ranges[a][1]])
            if verbose >= 2:
                print(f' Merging {ranges[a]} and {ranges[a+1]} to {ranges_return[-1]}')
            a += 1
        else:
            ranges_return.append(ranges[a])
        a += 1
    if ranges_return[-1][1] != ranges[-1][1]: # sloppy but effective
        ranges_return.append(ranges[-1])

    return ranges_return, merges

is_ranges = True
ranges = []
ingredients = set()
for line in lines:
    if line.rstrip() == '':
        is_ranges = False
        continue
    if is_ranges:
        parts = line.rstrip().split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append([start,end])
    else:
        ingredient = int(line.rstrip())
        ingredients.add(ingredient)

latest_merges = 1 # initialize to enter the loop
while latest_merges > 0:
    ranges, latest_merges = merge_ranges(ranges)
    if verbose >= 3:
        print(f'Updated ranges this pass: {ranges}')
    if verbose >= 1:
        print(f' After merging, {len(ranges)} ranges remain.')

num_covered = 0
for region in ranges:
    num_covered += region[1] - region[0] + 1

print('Done.')
print(f'  Number of ingredient IDs: {num_covered}')

## SANITY CHECK FROM PREVIOUS PART ##
 
# fresh_ones = 0
# for ingredient in ingredients:
#     for region in ranges: # calling it region to avoid breaking "range"
#         if ingredient >= region[0] and ingredient <= region[1]:
#             if verbose >= 3:
#                 print(f'ingredient {ingredient} is fresh')
#             fresh_ones += 1
#             break

# print('Done.')
# print(f'  Number of fresh ingredients: {fresh_ones}')