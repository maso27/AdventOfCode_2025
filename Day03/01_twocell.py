filename = './Day03/input.txt'
verbose = 0

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

best_sums = []

for line in lines:
    line = line.rstrip()
    high_num1 = 0
    high_loc1 = 0
    high_num2 = 0
    high_loc2 = 0
    for a, val in enumerate(line[:-1]): # skip last number
        num = int(val)
        if num > high_num1:
            high_num1 = num
            high_loc1 = a
            if verbose >= 3:
                print(f"  New high number {high_num1} at position {a} in line: {line}")
    if verbose >= 2:
        print(f"Line highest number: {high_num1} at position {high_loc1}\n")
    for b in range(high_loc1+1, len(line)):
        num = int(line[b])
        if num > high_num2:
            high_num2 = num
            high_loc2 = b
            if verbose >= 3:
                print(f"  New second high number {high_num2} at position {b} in line: {line}")
    if verbose >= 2:
        print(f"Line second highest number: {high_num2} at position {high_loc2}\n")
    best_sums.append(high_num1*10 + high_num2)

print(f"\nDone.")
if verbose >= 1:
    print(f"  Best sums per line: {best_sums}")
print(f"Total of best sums: {sum(best_sums)}\n")