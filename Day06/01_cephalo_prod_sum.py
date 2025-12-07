filename = './Day06/input.txt'
verbose = 0

import numpy as np

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

problems = []
for line in lines:
    problems.append(line.split())

operators = problems.pop()

if verbose >= 2:
    for row in problems:
        print(row)
    print(operators)

problems_t = np.array(problems).T.astype(int)

answers = []
for a, problem in enumerate(problems_t):
    if operators[a] == '*':
        answers.append(np.prod(problem))
    elif operators[a] == '+':
        answers.append(np.sum(problem))

if verbose >= 2:
    print(answers)

print('\nDone.')
print(f'Sum of answers: {np.sum(answers)}')
