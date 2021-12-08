inp = ''.join(open('aoc_1.txt'))

nums = list(map(int, inp.split('\n')))

it1, it2, it3 = iter(nums), iter(nums), iter(nums)
next(it2); next(it3); next(it3)

sums = [a + b + c for a, b, c in zip(it1, it2, it3)]

count = 0

for i in range(len(sums) - 1):
    count += sums[i + 1] > sums[i]

print(count)