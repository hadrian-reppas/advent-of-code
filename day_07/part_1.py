def dist(nums, n):
    return sum(abs(x - n) for x in nums)

nums = [int(n) for n in next(open('input.txt')).split(',')]

min_fuel = float('inf')
for i in range(max(nums)):
    min_fuel = min(dist(nums, i), min_fuel)

print(min_fuel)