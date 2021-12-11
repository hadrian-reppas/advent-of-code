from part_1 import step
from itertools import count

inp = ''.join(open('input.txt'))
nums = [[int(c) for c in row] for row in inp.split('\n')]

for i in count(1):
    if step(nums) == 100:
        print(i)
        break