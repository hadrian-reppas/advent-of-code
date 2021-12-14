def yslice(arr, row):
    top = arr[:row]
    bottom = arr[row + 1:2*row + 1]
    return top, bottom[::-1]

def xslice(arr, col):
    left = [row[:col] for row in arr]
    right = [row[col + 1:2*col + 1][::-1] for row in arr]
    return left, right

def arr_or(a, b):
    return [[x or y for x, y in zip(ar, br, strict=True)] for ar, br in zip(a, b, strict=True)]

def do(arr, cmd):
    match cmd:
        case ['x', row]:
            return arr_or(*xslice(arr, row))
        case ['y', col]:
            return arr_or(*yslice(arr, col))

def main():
    inp = ''.join(open('input.txt'))
    pts, oth = inp.split('\n\n')
    points = [tuple(int(x) for x in line.split(',')) for line in pts.split('\n')]
    commands = [(line[11], int(line[13:])) for line in oth.split('\n')]

    arr = [[False for _ in range(2000)] for _ in range(2000)]

    for r, c in points:
        arr[c][r] = True

    arr = do(arr, commands[0])

    count = sum(sum(row) for row in arr)
    print(count)

if __name__ == '__main__':
    main()