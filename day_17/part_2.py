from part_1 import test

line, = open('input.txt')

x_range = line[15:line.find(',')]
y_range = line[line.rfind('=') + 1:]
min_x, max_x = (int(n) for n in x_range.split('..'))
min_y, max_y = (int(n) for n in y_range.split('..'))

hits = 0

for vy in range(-min_y, min_y - 1, -1):
    for vx in range(max_x + 1):
        hits += test(vx, vy, min_x, max_x, min_y, max_y)

print(hits)