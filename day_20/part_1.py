import numpy as np
from scipy.signal import convolve2d

kernel = np.array([[  1,   2,   4],
                   [  8,  16,  32],
                   [ 64, 128, 256]])

def step(arr, fill, rule):
    # this isn't hard to implement, but using scipy is way faster
    out = rule[convolve2d(arr, kernel, fillvalue=fill)]
    out_fill = rule[-1 if fill else 0]
    return out, out_fill

def main():
    alg, board = ''.join(open(('input.txt'))).split('\n\n')
    rule = np.array([c == '#' for c in alg])
    arr = np.array([[c == '#' for c in row] for row in board.split('\n')])

    x, fill = step(arr, False, rule)
    x, fill = step(x, fill, rule)

    print(np.sum(x))

if __name__ == '__main__':
    main()