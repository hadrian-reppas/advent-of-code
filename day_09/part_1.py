inp = ''.join(open('input.txt'))
nums = [[int(x) for x in line] for line in inp.split('\n')]

total = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if ((i == 0 or nums[i - 1][j] > nums[i][j]) 
        and (j == 0 or nums[i][j - 1] > nums[i][j]) 
        and (i == len(nums) - 1 or nums[i + 1][j] > nums[i][j]) 
        and (j == len(nums[0]) - 1 or nums[i][j + 1] > nums[i][j])):
            total += nums[i][j] + 1

print(total)