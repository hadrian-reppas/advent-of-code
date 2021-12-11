inp = ''.join(open('input.txt'))
lines = [[[int(x) for x in pt.split(',')] for pt in line.split(' -> ')] for line in inp.split('\n')]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    x, y = min(line[0][0], line[1][0]), min(line[0][1], line[1][1])
    if line[0][0] == line[1][0]: # vertical
        while y <= max(line[0][1], line[1][1]):
            grid[y][x] += 1
            y += 1
    elif line[0][1] == line[1][1]: # horizontal
        while x <= max(line[0][0], line[1][0]):
            grid[y][x] += 1
            x += 1
    elif (line[0][0] < line[1][0] and line[0][1] < line[1][1] or
          line[0][0] > line[1][0] and line[0][1] > line[1][1]):
        while x <= max(line[0][0], line[1][0]):
            grid[y][x] += 1
            x += 1
            y += 1
    else:
        y = max(line[0][1], line[1][1])
        while x <= max(line[0][0], line[1][0]):
            grid[y][x] += 1
            x += 1
            y -= 1

n = 0

for row in grid:
    for x in row:
        if x >= 2:
            n += 1

print(n)
