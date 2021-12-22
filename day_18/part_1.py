from math import ceil

class num:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __add__(self, other):
        return num(self.copy(), other.copy()).reduce()
    def __radd__(self, other):
        return self
    def reduce(self):
        while self.explode() or self.split():
            pass
        return self
    def explode(self):
        return self.search() is not False
    def search(self, depth=0):
        if depth >= 3 and isinstance(self.left, num) and self.left.is_leaf():
            l, r = self.left.left, self.left.right
            self.left = 0
            self.update_right(r)
            return l, None
        if depth >= 3 and isinstance(self.right, num) and self.right.is_leaf():
            l, r = self.right.left, self.right.right
            self.right = 0
            self.update_left(l)
            return None, r
        if isinstance(self.left, num):
            x = self.left.search(depth + 1)
            if x is True:
                return True
            elif isinstance(x, tuple):
                l, r = x
                if l is None:
                    self.update_right(r)
                    return True
                else:
                    return x
        if isinstance(self.right, num):
            x = self.right.search(depth + 1)
            if x is True:
                return True
            elif isinstance(x, tuple):
                l, r = x
                if r is None:
                    self.update_left(l)
                    return True
                else:
                    return x
        return False
    def is_leaf(self):
        return isinstance(self.left, int) and isinstance(self.right, int)
    def update_right(self, val):
        if isinstance(self.right, int):
            self.right += val
        else:
            self.right.add_left(val)
    def add_left(self, val):
        if isinstance(self.left, int):
            self.left += val
        else:
            self.left.add_left(val)
    def update_left(self, val):
        if isinstance(self.left, int):
            self.left += val
        else:
            self.left.add_right(val)
    def add_right(self, val):
        if isinstance(self.right, int):
            self.right += val
        else:
            self.right.add_right(val)
    def split(self):
        if isinstance(self.left, int):
            if self.left >= 10:
                self.left = num(self.left//2, ceil(self.left/2))
                return True
        else:
            if self.left.split():
                return True
        if isinstance(self.right, int):
            if self.right >= 10:
                self.right = num(self.right//2, ceil(self.right/2))
                return True
        else:
            if self.right.split():
                return True
        return False
    def magnitude(self):
        mag = 0
        if isinstance(self.left, int):
            mag += 3*self.left
        else:
            mag += 3*self.left.magnitude()
        if isinstance(self.right, int):
            mag += 2*self.right
        else:
            mag += 2*self.right.magnitude()
        return mag
    def copy(self):
        l_copy = self.left if isinstance(self.left, int) else self.left.copy()
        r_copy = self.right if isinstance(self.right, int) else self.right.copy()
        return num(l_copy, r_copy)
    @staticmethod
    def parse(line):
        if line.isdecimal():
            return int(line)
        depth = i = 0
        for c in line:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c == ',' and depth == 1:
                break
            i += 1
        return num(num.parse(line[1:i]),
                   num.parse(line[i + 1:-1]))

def main():
    inp = ''.join(open('input.txt'))
    nums = [num.parse(line) for line in inp.split('\n')]

    n = sum(nums)
    print(n.magnitude())

if __name__ == '__main__':
    main()