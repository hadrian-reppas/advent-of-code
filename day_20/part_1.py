import numpy as np

def step(arr, in_fill, rule):
    big = np.full((len(arr) + 4, len(arr[0]) + 4), in_fill)
    big[2:-2, 2:-2] = arr
    out_fill = rule[-1 if in_fill else 0]
    out = np.zeros((len(arr) + 2, len(arr[0]) + 2), dtype=bool)
    for i in range(1, len(big) - 1):
        for j in range(1, len(big[0]) - 1):
            k = 0
            for a in (-1, 0, 1):
                for b in (-1, 0, 1):
                    k = (k << 1) | big[i + a][j + b]
            out[i - 1][j - 1] = rule[k]
    return out, out_fill

def main():
    inp = ''.join(open(('input.txt')))
    alg, board = inp.split('\n\n')
    arr = np.array([[c == '#' for c in row] for row in board.split('\n')])
    rule = np.array([c == '#' for c in alg])

    x, x_fill = step(arr, False, rule)
    x, x_fill = step(x, x_fill, rule)

    print(np.sum(x))

if __name__ == '__main__':
    main()