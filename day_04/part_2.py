from part_1 import board

def go(boards, n):
    i = 0
    while i < len(boards):
        if boards[i](n):
            del boards[i]
        else:
            i += 1

nums, boards = board.parse('input.txt')

nit = iter(nums)

while len(boards) > 1:
    go(boards, next(nit))

b, = boards

while not (x := b(next(nit))):
    pass

print(x)