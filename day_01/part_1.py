inp = ''.join(open('input.txt'))

nums = [int(n) for n in inp.split('\n')]
count = 0

for i in range(len(nums) - 1):
    count += nums[i + 1] > nums[i]

print(count)