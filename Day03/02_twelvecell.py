filename = './Day03/input.txt'
verbose = 0

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

num_digits = 12

best_sums = []

for line in lines:
    line = line.rstrip()
    high_num = [0] * num_digits
    high_loc = [0] * (num_digits + 1)
    for a in range(num_digits):
        for b in range(high_loc[a],len(line)-(num_digits - a - 1)):
            num = int(line[b])
            if num > high_num[a]:
                high_num[a] = num
                high_loc[a] = b
                if verbose >= 3:
                    print(f"  Digit {a}: New high number {high_num[a]} at position {b} in line: {line}")
        high_loc[a+1] = high_loc[a] + 1
    best_sum = 0
    for a in range(num_digits):
        best_sum += high_num[a] * (10 ** (num_digits - a - 1))
    best_sums.append(best_sum)

print(f"\nDone.")
if verbose >= 1:
    print(f"  Best sums per line: {best_sums}")
print(f"Total of best sums: {sum(best_sums)}\n")