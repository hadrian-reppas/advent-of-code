inp = ''.join(open('input.txt'))

x = y = aim = 0

for line in inp.split('\n'):
    c, n = line.split(' ')
    n = int(n)
    match c:
        case 'forward':
            x += n
            y += n*aim
        case 'down':
            aim += n
        case 'up':
            aim -= n

print(x*y)