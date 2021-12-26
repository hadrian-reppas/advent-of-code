def south(i, j, arr):
    return (i + 1) % len(arr), j

def east(i, j, arr):
    return i, (j + 1) % len(arr[0])

def step(arr):
    out = [[0 for x in row] for row in arr]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 1: continue
            a, b = east(i, j, arr)
            if arr[a][b] == 0:
                out[a][b] = 1
            else:
                out[i][j] = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 2: continue
            a, b = south(i, j, arr)
            if arr[a][b] != 2 and out[a][b] == 0:
                out[a][b] = 2
            else:
                out[i][j] = 2
    return out

inp = ''.join(open('input.txt'))
arr = [[{'.': 0, '>': 1, 'v': 2}[c] for c in line] for line in inp.split('\n')]

i = 1
while arr != (arr := step(arr)):
    i += 1

print(i)