filename = './Day01/input.txt'
verbose = 0

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

needlepoint = 50
num_zeros = 0

def algorithm(start, step, direction):
    if verbose >= 3:
        print(f'Start: {start}\tStep: {step}\tDir: {direction}')

    num_zeros = 0
    
    while step >= 100: # simplify large numbers
        step -= 100
        num_zeros += 1

    if direction.upper() == 'L': # turn left
        end = start - step
        if end <= 0:
            num_zeros += 1
        if start == 0:
            num_zeros -= 1
    else:                        # turn right
        end = start + step
        if end >= 100:
            num_zeros += 1
    
    end = end % 100

    if verbose >= 3:
        print(f'\tEnd: {end}\tNum Zeros: {num_zeros}')
    
    return end, num_zeros


for line in lines:
    turn_dir = line[0] # grab the first character
    clicks = int(line[1:])
    needlepoint, new_zeros = algorithm(needlepoint, clicks, turn_dir)
    num_zeros += new_zeros

    if verbose >= 2:
        print(f" num_zeros = {num_zeros}")

print(f"\nDone.\n  Total zero hits: {num_zeros}\n")
