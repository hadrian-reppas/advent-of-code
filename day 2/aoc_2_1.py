inp = ''.join(open('aoc_2.txt'))

x = y = 0

for line in inp.split('\n'):
    c, n = line.split(' ')
    n = int(n)
    match c:
        case 'forward':
            x += n
        case 'down':
            y += n
        case 'up':
            y -= n

print(x*y)