from part_1 import *

def print_arr(arr):
    for row in arr:
        for x in row:
            print('##' if x else '  ', end='')
        print()

inp = ''.join(open('input.txt'))
pts, oth = inp.split('\n\n')
points = [tuple(int(x) for x in line.split(',')) for line in pts.split('\n')]
commands = [(line[11], int(line[13:])) for line in oth.split('\n')]

arr = [[False for _ in range(2000)] for _ in range(2000)]

for x, y in points:
    arr[y][x] = True

for cmd in commands:
    arr = do(arr, cmd)

print_arr(arr)