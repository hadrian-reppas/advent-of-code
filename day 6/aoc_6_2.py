def step(arr):
    zeros = arr[0]
    for i in range(8):
        arr[i] = arr[i + 1]
    arr[6] += zeros
    arr[8] = zeros

nums = map(int, next(open('aoc_6.txt')).split(','))

arr = [0]*9
for n in nums:
    arr[n] += 1

for _ in range(256):
    step(arr)

print(sum(arr))