di_dj = [(-1, -1), (-1, 0,),  (-1, 1),
          (0, -1),             (0, 1),
          (1, -1),   (1, 0),   (1, 1)]

def update(nums, i, j):
    if nums[i][j] == -1:
        return
    nums[i][j] += 1
    if nums[i][j] <= 9:
        return
    nums[i][j] = -1
    for di, dj in di_dj:
        if (0 <= i + di < len(nums)
        and 0 <= j + dj < len(nums[0])):
            update(nums, i + di, j + dj)

def step(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            update(nums, i, j)
    x = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == -1:
                x += 1
                nums[i][j] = 0
    return x

def main():
    inp = ''.join(open('input.txt'))
    nums = [[int(c) for c in row] for row in inp.split('\n')]

    tot = 0
    for _ in range(100):
        tot += step(nums)
    print(tot)

if __name__ == '__main__':
    main()