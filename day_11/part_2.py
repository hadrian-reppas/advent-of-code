from part_1 import step
from itertools import count

inp = ''.join(open('input.txt'))
nums = [[int(c) for c in row] for row in inp.split('\n')]

i = 1
while step(nums) != 100:
    i += 1

print(i)