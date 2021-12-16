inp = ''.join(open('input.txt'))
nums = [[int(n) for n in line] for line in inp.split('\n')]

rows, cols = len(nums), len(nums[0])

nums[0][0] = 0

for i in range(rows - 2, -1, -1):
    nums[i][-1] += nums[i + 1][-1]
for j in range(cols - 2, -1, -1):
    nums[-1][j] += nums[-1][j + 1]

for i in range(rows - 2, -1, -1):
    for j in range(cols - 2, -1, -1):
        nums[i][j] += min(nums[i + 1][j], nums[i][j + 1])

print(nums[0][0])