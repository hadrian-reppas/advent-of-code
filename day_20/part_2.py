import numpy as np
from part_1 import step

alg, board = ''.join(open(('input.txt'))).split('\n\n')
rule = np.array([c == '#' for c in alg])
arr = np.array([[c == '#' for c in row] for row in board.split('\n')])

x, fill = arr, False
for _ in range(50):
    x, x_fill = step(x, fill, rule)

print(np.sum(x))