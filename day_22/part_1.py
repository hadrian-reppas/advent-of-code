def points(bounds):
    (min_x, max_x), (min_y, max_y), (min_z, max_z) = bounds
    for x in range(max(-50, min_x), min(50, max_x) + 1):
        for y in range(max(-50, min_y), min(50, max_y) + 1):
            for z in range(max(-50, min_z), min(50, max_z) + 1):
                yield x, y, z

inp = ''.join(open('input.txt'))
regions = [(line.split(' ')[0], tuple((int(a[2:].split('..')[0]), int(a[2:].split('..')[1])) for a in line.split(' ')[1].split(','))) for line in inp.split('\n')]

on = set()

for cmd, bounds in regions:
    if cmd == 'on':
        for pt in points(bounds):
            on.add(pt)
    elif cmd == 'off':
        for pt in points(bounds):
            if pt in on:
                on.remove(pt)
    else:
        assert False

print(len(on))