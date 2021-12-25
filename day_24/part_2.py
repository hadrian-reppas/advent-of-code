from part_1 import get_possibilities

def get_min(possible):
    n = 0
    for lo, hi in possible:
        n = 10*n + lo
    return n

inp = ''.join(open('input.txt'))
code = [line.split(' ') for line in inp.split('\n')]
a_list = [int(a) for _, _, a in code[4::18]]
b_list = [int(b) for _, _, b in code[5::18]]
c_list = [int(c) for _, _, c in code[15::18]]

possible = get_possibilities(a_list, b_list, c_list)

print(get_min(possible))