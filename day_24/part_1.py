'''
I have not bothered to explain any of my other solutions, but this ons is so
questionable I fell like I need to.

My answer hinges on the fact that the sequence of instructions is 14 copies
of the same 18 instructions:

```
inp w
mul x 0
add x z
mod x 26
div z a
add x b
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y c
add y w
add y 9
mul y x
add z y
```

where `a`, `b` and `c` change each repitition. Written in python:

```
z = 0
for input, a, b, c in zip(inputs, a_list, b_list, c_list):
    z = z//a if z % 26 + b == input else 26*(z//a) + c + input
```

For my input, 

```
a_list = [  1,   1,   1,   1,  26,   1,   1,  26,   1,  26,  26,  26,  26,  26]
b_list = [ 15,  11,  10,  12, -11,  11,  14,  -6,  10,  -6,  -6, -16,  -4,  -2]
c_list = [  9,   1,  11,   3,  10,   5,   0,   7,   9,  15,   4,  10,   4,   9]
```

Notice that on the first loop, the `z % 26 + b == input` test will always be
`False` because `1 <= input <= 9` and `0 % 26 + b` is `15`, which is greater
than `9`. `z` then becomes `c + input`, which is `9 + inputs[0]`. Notice again
that the `z % 26 + b == input` test will be `False` because `10 <= z <= 18`, so 
`z % 26 + b` is between `21` and `29`, which is greater than any possible input.

But if `inputs[4] == inputs[3] - 8`, the condition evaluates to `True`. So our
analysis branches: one case has `inputs[4] == inputs[3] - 8` and the other where
`inputs[4] != inputs[3] - 8`.

The three classes I define keep track of these possibilities. In the first case
above, inputs[4] is represented as `inp_range(4, 9, 9)` and inputs[3] is
represented as `inp_range(3, 1, 1)`. In the second, `inputs[4]` is represented
as `inp_range(4, 1, 9, inp_offset(inp_range(3, 1, 9), -8)`. This ensures
that on the branch being examined, `inputs[4]` and `inputs[3]` can be any number
`1` to `9` except a combination where `inputs[4] == inputs[3] - 8`. The `lin_inp`
class represents a linear combination of `inp_range`s. At every step, z is
defined as a linear combination of inputs.

The `analyze` function examines every possible branch and finds the one where
`z == 0` is possible (There happens to only be one in my input. Not sure if this
is always true). It then breaks apart the restrictions and returns a `list` of
`tuple`s representing the restrictions to ensure `z == 0`. Using the example
above, `inputs[4] == inputs[3] - 8' must be `True` if we want `z` to be `0`. So
in the `list` `analyze` returns, we would find `(4, 3, -8)` to represent the fact
that `inputs[4] == inputs[3] - 8'.

For my input, we get:

```
i4 = i3 + -8
i7 = i6 + -6
i9 = i8 + 3
i10 = i5 + -1
i11 = i2 + -5
i12 = i1 + -3
i13 = i0 + 7
```

where `i8` is shorthand for `inputs[8]`. Our task is then to maximize/minimize
the number subject to these constrains. The `find_possibilities` returns each
input's min and max possibilities. And the `get_max` function returns the largest
model number from these possibilities.

This code is garbage. I made many assumptions that work for my input but may not
be true for any input. In a previous commit, you can see older code that contained
a bunch of assert statements which made sure my assumptions were true. But I removed
them so the current code will likely fail silently.
'''

class inp_range:
    def __init__(self, i, lo=1, hi=9, not_=set()):
        self.i = i
        self.lo = lo
        self.hi = hi
        self.not_ = not_
    def add_not(self, not_):
        return inp_range(self.i, self.lo, self.hi, self.not_ | {not_})

class inp_offset:
    def __init__(self, i, const):
        self.i = i
        self.const = const

class lin_inp:
    def __init__(self, const, coeffs=(), inps=()):
        self.const = const
        self.coeffs = coeffs
        self.inps = inps
    def add(self, coeff, inp):
        return lin_inp(self.const, self.coeffs + (coeff,), self.inps + (inp,))
    def add_const(self, const):
        return lin_inp(self.const + const, self.coeffs, self.inps)
    def mod_26(self):
        new_const = self.const % 26
        new_coeffs = []
        new_inps = []
        for coeff, inp in zip(self.coeffs, self.inps):
            if coeff % 26:
                new_coeffs.append(coeff % 26)
                new_inps.append(inp)
        without_mod = lin_inp(new_const, tuple(new_coeffs), tuple(new_inps))
        return without_mod
    def div_26(self):
        new_coeffs = []
        new_inps = []
        one_inp = None
        for coeff, inp in zip(self.coeffs, self.inps):
            if coeff > 1:
                new_coeffs.append(coeff//26)
                new_inps.append(inp)
            else:
                one_inp = inp
        if one_inp:
            lo = (self.const + one_inp.lo)//26
            hi = (self.const + one_inp.hi)//26
            return lin_inp(lo, tuple(new_coeffs), tuple(new_inps))
        return lin_inp(self.const//26, tuple(new_coeffs), tuple(new_inps))
    def times_26(self):
        new_const = 26*self.const
        new_coeffs = tuple(26*c for c in self.coeffs)
        return lin_inp(new_const, new_coeffs, self.inps)
    def overlap(self, other):
        if len(self.coeffs) == 0:
            if other.lo <= self.const <= other.hi:
                return None, inp_range(self.const, self.const)
            return None
        lo = max(self.inps[0].lo, other.lo - self.const)
        hi = min(self.inps[0].hi, other.hi - self.const)
        if lo <= hi:
            s_inp_r = inp_range(self.inps[0].i, lo, hi)
            o_inp_r = inp_offset(s_inp_r, self.const)
            return other.add_not(o_inp_r)

def analyze(prev_z, index, a_list, b_list, c_list):
    if index == 14:
        if prev_z.const == 0:
            return []
        return
    z_mod_26_plus_b = prev_z.mod_26().add_const(b_list[index])
    next_inp = inp_range(index)
    next_inp_st_condition_false = z_mod_26_plus_b.overlap(next_inp)
    z_prev_div_a = prev_z.div_26() if a_list[index] == 26 else prev_z
    if next_inp_st_condition_false is None:
        z = z_prev_div_a.times_26().add(1, next_inp).add_const(c_list[index])
        x = analyze(z, index + 1, a_list, b_list, c_list)
        if isinstance(x, list):
            return x
    else:
        z_condition_false = z_prev_div_a.times_26().add(1, next_inp_st_condition_false).add_const(c_list[index])
        z_condition_true = z_prev_div_a
        x = analyze(z_condition_false, index + 1, a_list, b_list, c_list)
        if isinstance(x, list):
            n = next_inp_st_condition_false
            m, = n.not_
            # x.append(f'i{n.i} != i{m.i.i} + {m.const}')
            x.append((n.i, m.i.i, m.const, 'not'))
            return x
        y = analyze(z_condition_true, index + 1, a_list, b_list, c_list)
        if isinstance(y, list):
            n = next_inp_st_condition_false
            m, = n.not_
            # y.append(f'i{n.i} = i{m.i.i} + {m.const}')
            y.append((n.i, m.i.i, m.const))
            return y

def find_possibilities(restrictions):
    assert max(len(r) for r in restrictions) == 3
    possible = [[1, 9] for _ in range(14)]
    for i in range(14):
        for r in restrictions:
            left_i, right_i, offset = r
            if left_i != i and right_i != i:
                continue
            if offset < 0:
                possible[left_i][1] = min(9 + offset, possible[left_i][1])
                possible[right_i][0] = max(1 - offset, possible[right_i][0])
            else:
                possible[right_i][1] = min(9 - offset, possible[right_i][1])
                possible[left_i][0] = max(1 + offset, possible[left_i][0])
    return possible

def get_max(possible):
    n = 0
    for lo, hi in possible:
        n = 10*n + hi
    return n

def get_possibilities(a_list, b_list, c_list):
    restrictions = analyze(lin_inp(0), 0, a_list, b_list, c_list)
    return find_possibilities(restrictions)

def main():
    inp = ''.join(open('input.txt'))
    code = [line.split(' ') for line in inp.split('\n')]
    a_list = [int(a) for _, _, a in code[4::18]]
    b_list = [int(b) for _, _, b in code[5::18]]
    c_list = [int(c) for _, _, c in code[15::18]]

    possible = get_possibilities(a_list, b_list, c_list)

    print(get_max(possible))

if __name__ == '__main__':
    main()