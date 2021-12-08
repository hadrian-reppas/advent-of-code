inp = ''.join(open('aoc_5.txt'))
ls = [[[int(x) for x in pt.split(',')] for pt in line.split(' -> ')] for line in inp.split('\n')]
lines = [l for l in ls if l[0][0] == l[1][0] or l[0][1] == l[1][1]]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    x, y = min(line[0][0], line[1][0]), min(line[0][1], line[1][1])
    if line[0][0] == line[1][0]: # vertical
        while y <= max(line[0][1], line[1][1]):
            grid[y][x] += 1
            y += 1
    else: # horizontal
        while x <= max(line[0][0], line[1][0]):
            grid[y][x] += 1
            x += 1

n = 0

for row in grid:
    for x in row:
        if x >= 2:
            n += 1

print(n)