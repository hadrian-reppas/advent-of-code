class board:
    def __init__(self, s):
        self.board = [[int(n) + 1 for n in l.split(' ') if n] for l in s.split('\n')]
    def __call__(self, n):
        for row in self.board:
            while n in row:
                row[row.index(n)] = 0
        if self.win():
            return self.total()*(n - 1)
        return 0
    def win(self):
        for row in self.board:
            if sum(row) == 0:
                return True
        for i in range(5):
            if sum(self.board[j][i] for j in range(5)) == 0:
                return True
        return False
    def total(self):
        x = 0
        for row in self.board:
            x += sum(y - 1 for y in row if y)
        return x
    @staticmethod
    def parse(file_name):
        it = iter(''.join(open(file_name)).split('\n\n'))
        nums = [int(x) + 1 for x in next(it).split(',')]
        boards = [board(b) for b in it]
        return nums, boards

def main():
    nums, boards = board.parse('input.txt')

    for n in nums:
        for b in boards:
            if (x := b(n)):
                return x

if __name__ == '__main__':
    print(main())