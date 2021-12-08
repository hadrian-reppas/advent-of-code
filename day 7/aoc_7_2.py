def dist(nums, n):
    return sum(triangle(abs(x - n)) for x in nums)

def triangle(n):
    return n*(n + 1)//2

nums = [int(n) for n in next(open('aoc_7.txt')).split(',')]

min_fuel = float('inf')
for i in range(1877):
    min_fuel = min(dist(nums, i), min_fuel)

print(min_fuel)