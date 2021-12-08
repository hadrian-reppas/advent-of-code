inp = ''.join(open('aoc_1.txt'))

nums = list(map(int, inp.split('\n')))
count = 0

for i in range(len(nums) - 1):
    count += nums[i + 1] > nums[i]

print(count)