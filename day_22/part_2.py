inp = ''.join(open('input.txt'))
regions = [(line.split(' ')[0], tuple((int(a[2:].split('..')[0]), int(a[2:].split('..')[1])) for a in line.split(' ')[1].split(','))) for line in inp.split('\n')]

x_coords = sorted([x for _, ((x, _), _, _) in regions] + [x + 1 for _, ((_, x), _, _) in regions])
y_coords = sorted([y for _, (_, (y, _), _) in regions] + [y + 1 for _, (_, (_, y), _) in regions])
z_coords = sorted([z for _, (_, _, (z, _)) in regions] + [z + 1 for _, (_, _, (_, z)) in regions])

# this is really slow, ~10 minutes on my machine with CPython.
# you can find a C++ implementation that takes ~20 seconds in the misc directory
on = 0
for i, (x_min, x_max) in enumerate(zip(x_coords, x_coords[1:])):
    print(str(i).rjust(4) + f"/{len(x_coords)}")
    x_regions = [(cmd, ((xm, xM), ys, zs)) for cmd, ((xm, xM), ys, zs) in regions if xm <= x_min <= xM]
    for y_min, y_max in zip(y_coords, y_coords[1:]):
        y_regions = [(cmd, (xs, (ym, yM), zs)) for cmd, (xs, (ym, yM), zs) in x_regions if ym <= y_min <= yM]
        for z_min, z_max in zip(z_coords, z_coords[1:]):
            z_regions = [(cmd, (xs, ys, (zm, zM))) for cmd, (xs, ys, (zm, zM)) in y_regions if zm <= z_min <= zM]
            if z_regions and z_regions[-1][0] == 'on':
                on += (x_max - x_min)*(y_max - y_min)*(z_max - z_min)

print(on)