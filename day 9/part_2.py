inp = ''.join(open('input.txt'))
nums = [[int(x) for x in line] for line in inp.split('\n')]

counts = {}
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if ((i == 0 or nums[i - 1][j] > nums[i][j]) 
          & (j == 0 or nums[i][j - 1] > nums[i][j]) 
          & (i == len(nums) - 1 or nums[i + 1][j] > nums[i][j]) 
          & (j == len(nums[0]) - 1 or nums[i][j + 1] > nums[i][j])):
            counts[(i, j)] = 0

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if nums[i][j] == 9: continue
        a, b = i, j
        while (a, b) not in counts:
            if a > 0 and nums[a - 1][b] < nums[a][b]:
                a -= 1
            elif b > 0 and nums[a][b - 1] < nums[a][b]:
                b -= 1
            elif a < len(nums) - 1 and nums[a + 1][b] < nums[a][b]:
                a += 1
            elif b < len(nums[0]) - 1 and nums[a][b + 1] < nums[a][b]:
                b += 1
        counts[(a, b)] += 1

a, b, c = sorted(counts.values())[-3:]
print(a*b*c)