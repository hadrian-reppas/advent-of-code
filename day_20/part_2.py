import numpy as np
from part_1 import step

inp = ''.join(open(('input.txt')))
alg, board = inp.split('\n\n')
arr = np.array([[c == '#' for c in row] for row in board.split('\n')])
rule = np.array([c == '#' for c in alg])

x, x_fill = arr, False
for _ in range(50):
    x, x_fill = step(x, x_fill, rule)

print(np.sum(x))