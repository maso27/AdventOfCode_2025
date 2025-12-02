filename = './Day02/sample.txt'
verbose = 3

def find_pattern(num_str):
    num_length = len(num_str) # the length of the number
    if num_length % 2 != 0:
        return False
    pattern_length = int(num_length / 2) # the pattern would be repeated twice
    pattern = num_str[0:pattern_length]
    if pattern * 2 == num_str:
        return True
    return False
    # see if this is a future solution (it matches any pattern of any length)
    # i = (num_str + num_str).find(num_str, 1, -1)
    # return i != -1



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
