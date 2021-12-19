from part_1 import align_all

def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

inp = ''.join(open('sample.txt'))
data = [[tuple(int(n) for n in line.split(',')) for line in s.split('\n')[1:]]
            for s in inp.split('\n\n')]

scanners = []
align_all(data, scanners)

max_dist = max(manhattan(a, b) for a in scanners for b in scanners if a is not b)
print(max_dist)