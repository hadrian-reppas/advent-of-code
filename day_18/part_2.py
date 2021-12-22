from part_1 import num

inp = ''.join(open('input.txt'))
nums = [num.parse(line) for line in inp.split('\n')]

max_mag = 0

for a in nums:
    for b in nums:
        if a is not b:
            mag = (a + b).magnitude()
            max_mag = max(mag, max_mag)

print(max_mag)