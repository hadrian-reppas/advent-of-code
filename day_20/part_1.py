import numpy as np
from scipy.signal import convolve2d

kernel = np.array([[  1,   2,   4],
                   [  8,  16,  32],
                   [ 64, 128, 256]])

def step(arr, fill, rule):
    # this isn't hard to implement in Python, but using scipy is way faster
    out = rule[convolve2d(arr, kernel, fillvalue=fill)]
    out_fill = rule[-1 if fill else 0]
    return out, out_fill

def main():
    alg, board = ''.join(open(('input.txt'))).split('\n\n')
    arr = np.array([[c == '#' for c in row] for row in board.split('\n')])
    rule = np.array([c == '#' for c in alg])

    x, x_fill = step(arr, False, rule)
    x, x_fill = step(x, x_fill, rule)

    print(np.sum(x))

if __name__ == '__main__':
    main()