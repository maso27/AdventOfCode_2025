filename = './Day01/input.txt'
verbose = 3

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

needlepoint = 50
num_zeros = 0

for line in lines:
    turn_dir = line[0] # grab the first character
    clicks = int(line[1:])
    if verbose >= 2:
        print(f"  Turning {turn_dir} and moving {clicks} clicks from {needlepoint}", end='')
    if turn_dir.upper() == "L":
        clicks = -clicks
    needlepoint = (needlepoint + clicks) % 100
    if verbose >= 2:
        print(  f" to {needlepoint}")
    if needlepoint == 0:
        num_zeros += 1
        if verbose >= 1:
            print(f"Hit zero at line: {line}")

print(f"\nDone.\n  Total zero hits: {num_zeros}\n")