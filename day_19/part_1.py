rotations = ['', 'x', 'y', 'xx', 'xy', 'yx', 'yy', 'xxx', 'xxy', 'xyx',
             'xyy', 'yxx', 'yyx', 'yyy', 'xxxy', 'xxyx', 'xxyy',
             'xyxx', 'xyyy', 'yxxx', 'yyyx', 'xxxyx', 'xyxxx', 'xyyyx']

def rot_x(points):
    return [(x, -z, y) for x, y, z in points]

def rot_y(points):
    return [(-z, y, x) for x, y, z in points]

def rots(points):
    for r in rotations:
        pts = points
        for c in r:
            pts = rot_x(pts) if c == 'x' else rot_y(pts)
        yield pts

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def diff(a):
    d = {}
    for x in a:
        for y in a:
            if x is y: continue
            s = sub(x, y)
            assert s not in d
            d[s] = x, y
    return d

def align(a_points, b_points, scanners):
    a_diff = diff(a_points)
    a_diff_set = set(a_diff)
    for b_rot in rots(b_points):
        b_diff = diff(b_rot)
        intersect = a_diff_set & set(b_diff)
        if len(intersect) >= 24:
            i, *_ = intersect
            a_point = a_diff[i][0]
            b_point = b_diff[i][0]
            offset = sub(a_point, b_point)
            scanners.append(offset)
            return [add(x, offset) for x in b_rot]
    return False

def align_all(data, scanners=[]):
    points = set(data[0])
    todo = []
    scanners.append((0, 0, 0))

    for pts in data[1:]:
        anchor_points = tuple(points)
        aligned = align(anchor_points, pts, scanners)
        if aligned is False:
            todo.append(pts)
        else:
            points |= set(aligned)

    while todo:
        pts = todo.pop(0)
        anchor_points = tuple(points)
        aligned = align(anchor_points, pts, scanners)
        if aligned is False:
            todo.append(pts)
        else:
            points |= set(aligned)
    
    return points

def main():
    inp = ''.join(open('input.txt'))
    data = [[tuple(int(n) for n in line.split(',')) for line in s.split('\n')[1:]]
                 for s in inp.split('\n\n')]
    
    points = align_all(data)
    print(len(points))

if __name__ == '__main__':
    main()