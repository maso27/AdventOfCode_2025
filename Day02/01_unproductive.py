filename = './Day02/sample.txt'
verbose = 3

f = open(filename, 'r')
# lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

invalid_ids = []

ranges = line.split(',')
for range in ranges:
    ends = range.split('-')
    start = int(ends[0])
    stop = int(ends[1])
    # TODO: sort ints from start to stop looking for repeating patterns (123123123 etc)