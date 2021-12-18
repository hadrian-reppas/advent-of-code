def test(vx, vy, min_x, max_x, min_y, max_y):
    x = y = 0
    while x <= max_x and y >= min_y:
        x, y = x + vx, y + vy
        vx, vy = vx - bool(vx), vy - 1
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
    return False

def max_height(vy):
    return vy*(vy + 1)//2

def main():
    line, = open('input.txt')

    x_range = line[15:line.find(',')]
    y_range = line[line.rfind('=') + 1:]
    min_x, max_x = (int(n) for n in x_range.split('..'))
    min_y, max_y = (int(n) for n in y_range.split('..'))

    for vy in range(-min_y, -1, -1):
        for vx in range(max_x + 1):
            if test(vx, vy, min_x, max_x, min_y, max_y):
                print(max_height(vy))
                return
    assert False

if __name__ == '__main__':
    main()