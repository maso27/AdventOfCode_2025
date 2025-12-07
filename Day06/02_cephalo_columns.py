filename = './Day06/input.txt'
verbose = 0

import numpy as np

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

line_list = []
for line in lines:
    line_list.append(list(line[:-1]))
lines_t = np.array(line_list).T
if verbose >= 2:
    print(lines_t)

a = len(lines_t)
answers = []
temp_problem = []
while a > 0:
    a -= 1
    temp_int = 0
    is_number = False
    for ch in lines_t[a][:-1]:
        if ch != ' ':
            temp_int = temp_int * 10 + int(ch)
            is_number = True
    if is_number:
        temp_problem.append(temp_int)
    if lines_t[a][-1] == '+': # add the numbers
        answers.append(np.sum(temp_problem))
        temp_problem = []
    elif lines_t[a][-1] == '*': # multiply the numbers
        answers.append(np.prod(temp_problem))
        temp_problem = []

if verbose >= 2:
    print(f'Answers: {answers[::-1]}') # print answers in correct order

print('\nDone.')
print(f'Sum of answers: {np.sum(answers)}')
