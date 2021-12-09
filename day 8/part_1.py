inp = ''.join(open('input.txt'))

rhs = [line.split(' | ')[1].split(' ') for line in inp.split('\n')]

n = 0
for line in rhs:
    for x in line:
        n += len(x) in [2, 3, 4, 7]

print(n)