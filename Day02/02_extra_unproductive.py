filename = './Day02/input.txt'
verbose = 3

def find_pattern(num_str):
    i = (num_str + num_str).find(num_str, 1, -1)
    return i != -1



f = open(filename, 'r')
# lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

invalid_ids = []

id_ranges = line.split(',')
for id_range in id_ranges:
    ends = id_range.split('-')
    start = int(ends[0])
    stop = int(ends[1])
    for num in range(start, stop + 1):
        if find_pattern(str(num)):
            invalid_ids.append(num)
            if verbose >= 2:
                print(f"  Found invalid ID: {num}")

print(f"\nDone.\n  Total sum of invalid IDs: {sum(invalid_ids)}")
