from random import randint

class node:
    def __add__(self, other):
        return add(self, other)
    def __mul__(self, other):
        return mul(self, other)
    def __truediv__(self, other):
        return div(self, other)
    def __mod__(self, other):
        return mod(self, other)
    def simplify(self, depth=None):
        return self
    def eval(self, inps):
        assert False

class bop(node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f'({self.left}){ops[type(self)]}({self.right})'

class add(bop):
    def simplify(self, depth=None):
        if depth == 0: return self
        l = self.left.simplify(None if depth is None else depth - 1)
        r = self.right.simplify(None if depth is None else depth - 1)
        if l == 0:
            return r
        elif r == 0:
            return l
        elif isinstance(l, val) and isinstance(r, val):
            return val(l.i + r.i)
        return add(l, r)
    def eval(self, inps):
        return self.left.eval(inps) + self.right.eval(inps)
        
class mul(bop):
    def simplify(self, depth=None):
        if depth == 0: return self
        l = self.left.simplify(None if depth is None else depth - 1)
        r = self.right.simplify(None if depth is None else depth - 1)
        if l == 0 or r == 0:
            return val(0)
        elif l == 1:
            return r
        elif r == 1:
            return l
        elif isinstance(l, val) and isinstance(r, val):
            return val(l.i*r.i)
        return mul(l, r)
    def eval(self, inps):
        return self.left.eval(inps)*self.right.eval(inps)

class div(bop):
    def simplify(self, depth=None):
        if depth == 0: return self
        l = self.left.simplify(None if depth is None else depth - 1)
        r = self.right.simplify(None if depth is None else depth - 1)
        if l == 0:
            return val(0)
        elif r == 1:
            return l
        elif isinstance(l, val) and isinstance(r, val):
            return val(l.i//r.i)
        return div(l, r)
    def eval(self, inps):
        return self.left.eval(inps)//self.right.eval(inps)

class mod(bop):
    def simplify(self, depth=None):
        if depth == 0: return self
        l = self.left.simplify(None if depth is None else depth - 1)
        r = self.right.simplify(None if depth is None else depth - 1)
        if l == 0 or r == 1:
            return val(0)
        elif isinstance(l, val) and isinstance(r, val):
            return val(l.i%r.i)
        return mod(l, r)
    def eval(self, inps):
        return self.left.eval(inps)%self.right.eval(inps)

class eql(bop):
    def simplify(self, depth=None):
        if depth == 0: return self
        l = self.left.simplify(None if depth is None else depth - 1)
        r = self.right.simplify(None if depth is None else depth - 1)
        if isinstance(l, val) and isinstance(r, val):
            return val(int(l == r))
        if isinstance(l, eql) and isinstance(r, val):
            if r.i not in [0, 1]:
                return val(0)
        if isinstance(l, val) and isinstance(r, eql):
            if l.i not in [0, 1]:
                return val(0)
        if isinstance(l, inp) and isinstance(r, val):
            if r.i < 1 or 9 < r.i:
                return val(0)
        if isinstance(l, val) and isinstance(r, inp):
            if l.i < 1 or 9 < l.i:
                return val(0)
        if isinstance(l, val) and isinstance(r, val):
            return val(int(l.i == r.i))
        return eql(l, r)
    def eval(self, inps):
        return int(self.left.eval(inps) == self.right.eval(inps))

ops = {add: '+', mul: '*', div: '//', mod: '%', eql: '=='}

class uop(node):
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        if isinstance(self, inp):
            return f'i{self.i}'
        elif isinstance(self, val):
            return str(self.i)
    def __eq__(self, other):
        if isinstance(self, inp):
            return isinstance(other, inp) and self.i == other.i
        elif isinstance(self, val):
            if isinstance(other, val):
                return self.i == other.i
            elif isinstance(other, int):
                return self.i == other
            return False
    def eval(self, inps):
        if isinstance(self, inp):
            return inps[self.i]
        elif isinstance(self, val):
            return self.i

class inp(uop): pass
class val(uop): pass

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calc(code, inps):
    regs = {u: 0 for u in 'wxyz'}
    for cmd in code:
        if len(cmd) == 2:
            _, u = cmd
            regs[u] = inps.pop(0)
        else:
            op, u, v = cmd
            match op:
                case 'add':
                    regs[u] = regs[u] + (int(v) if is_int(v) else regs[v])
                case 'mul':
                    regs[u] = regs[u]*(int(v) if is_int(v) else regs[v])
                case 'mod':
                    regs[u] = regs[u]%(int(v) if is_int(v) else regs[v])
                case 'div':
                    regs[u] = regs[u]//(int(v) if is_int(v) else regs[v])
                case 'eql':
                    regs[u] = int(regs[u] == (int(v) if is_int(v) else regs[v]))
    return regs

inp_ = ''.join(open('input.txt'))
code = [tuple(line.split(' ')) for line in inp_.split('\n')]

regs = {u: val(0) for u in 'wxyz'}
inp_count = 0

for cmd in code:
    if len(cmd) == 2:
        _, u = cmd
        regs[u] = inp(inp_count)
        inp_count += 1
    else:
        op, u, v = cmd
        regs[u] = eval(op)(regs[u], val(int(v)) if is_int(v) else regs[v]).simplify(2)

'''
arr = [[' '.join(x for x in line).ljust(10) for line in code[i::18]] for i in range(18)]
for j in range(14):
    print(''.join(arr[i][j] for i in range(18)))
print()
print('inp w     mul x 0   add x z   mod x 26  div z a   add x b   eql x w   eql x 0   mul y 0   add y 25  mul y x   add y 1   mul z y   mul y 0   add y w   add y c   mul y x   add z y')
'''

a_list = [  1,   1,   1,   1,  26,   1,   1,  26,   1,  26,  26,  26,  26,  26]
b_list = [ 15,  11,  10,  12, -11,  11,  14,  -6,  10,  -6,  -6, -16,  -4,  -2]
c_list = [  9,   1,  11,   3,  10,   5,   0,   7,   9,  15,   4,  10,   4,   9]

p_ops = {'add': '+', 'mul': '*', 'div': '//', 'mod': '%', 'eql': '=='}
p_code = 'def calc2(inps):\n    w = x = y = z = 0\n' + '\n'.join('    w = inps.pop(0)' if len(line) == 2 else (f'    {line[1]} = {line[1]} {p_ops[line[0]]} {line[2]}') for line in code) + '\n    return z'

exec(p_code)

def calc3(inps):
    x = y = z = 0
    for i, a, b, c in zip(inps, a_list, b_list, c_list, strict=True):
        x *= 0
        x += z
        x %= 26
        z //= a
        x += b
        x = int(x == i)
        x = int(x == 0)
        y *= 0
        y += 25
        y *= x
        y += 1
        z *= y
        y *= 0
        y += i
        y += c
        y *= x
        z += y
    return z

def calc4(inps):
    z = 0
    for i, a, b, c in zip(inps, a_list, b_list, c_list):
       x = 0 if z % 26 + b == i else 1
       y = 0 if z % 26 + b == i else i + c
       z = (z//a if z % 26 + b == i else 26*(z//a) + i + c)
    return z

def calc5(inps):
    z = 0
    for i, a, b, c in zip(inps, a_list, b_list, c_list):
        assert z % 26 + b != i
        z = (z//a if z % 26 + b == i else 26*(z//a) + i + c)
        print(z)
    return z

#           0    1    2    3    4    5    6    7    8    9   10   11   12   13
a_list = [  1,   1,   1,   1,  26,   1,   1,  26,   1,  26,  26,  26,  26,  26]
b_list = [ 15,  11,  10,  12, -11,  11,  14,  -6,  10,  -6,  -6, -16,  -4,  -2]
c_list = [  9,   1,  11,   3,  10,   5,   0,   7,   9,  15,   4,  10,   4,   9]

class inp_range:
    def __init__(self, i, lo=1, hi=9, not_=set()):
        assert 1 <= lo <= 9
        assert 1 <= hi <= 9
        assert lo <= hi
        self.i = i
        self.lo = lo
        self.hi = hi
        self.not_ = not_
    def add_not(self, not_):
        return inp_range(self.i, self.lo, self.hi, self.not_ | {not_})
    def __repr__(self):
        s = f'i{self.i}[{self.lo},{self.hi}]'
        if self.not_: s += str(self.not_)
        return s

class inp_offset:
    def __init__(self, i, const):
        self.i = i
        self.const = const
    def __repr__(self):
        return f'<{self.i} + {self.const}>'

class lin_inp:
    def __init__(self, const, coeffs=(), inps=()):
        self.const = const
        self.coeffs = coeffs
        self.inps = inps
    def add(self, coeff, inp):
        return lin_inp(self.const, self.coeffs + (coeff,), self.inps + (inp,))
    def add_offset(self, inp_o):
        return lin_inp(self.const + inp_o.const, self.coeffs + (1,), self.inps + (inp_o.i,))
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
        assert 0 <= without_mod.min() and without_mod.max() < 26
        return without_mod
    def div_26(self):
        new_coeffs = []
        new_inps = []
        one_inp = None
        for coeff, inp in zip(self.coeffs, self.inps):
            if coeff > 1:
                assert coeff % 26 == 0
                new_coeffs.append(coeff//26)
                new_inps.append(inp)
            else:
                one_inp = inp
        if one_inp:
            lo = (self.const + one_inp.lo)//26
            hi = (self.const + one_inp.hi)//26
            assert lo == hi
            return lin_inp(lo, tuple(new_coeffs), tuple(new_inps))
        return lin_inp(self.const//26, tuple(new_coeffs), tuple(new_inps))
    def times_26(self):
        new_const = 26*self.const
        new_coeffs = tuple(26*c for c in self.coeffs)
        return lin_inp(new_const, new_coeffs, self.inps)
    def min(self):
        x = self.const
        for coeff, inp in zip(self.coeffs, self.inps):
            x += coeff*inp.lo
        return x
    def max(self):
        x = self.const
        for coeff, inp in zip(self.coeffs, self.inps):
            x += coeff*inp.hi
        return x
    def overlap(self, other):
        assert isinstance(other, inp_range)
        if len(self.coeffs) == 0:
            if other.lo <= self.const <= other.hi:
                return None, inp_range(self.const, self.const)
            return None
        assert self.coeffs[0] == 1
        lo = max(self.inps[0].lo, other.lo - self.const)
        hi = min(self.inps[0].hi, other.hi - self.const)
        if lo <= hi:
            s_inp_r = inp_range(self.inps[0].i, lo, hi)
            o_inp_r = inp_offset(s_inp_r, self.const)
            # return (s_inp_r, o_inp_r), other.add_not(o_inp_r)
            return other.add_not(o_inp_r)
    def insert(self, vals):
        # vals[inp_range | tuple[int, int]]
        new_const = self.const
        new_inps = list(self.inps)
        new_coeffs = list(self.coeffs)
        for v in vals:
            for i in range(len(new_coeffs)):
                if isinstance(v, inp_range) and v.i == new_inps[i].i:
                    new_inps[i] = v
                    break
                elif isinstance(v, tuple) and v[0] == new_inps[i].i:
                    new_const += new_coeffs[i]*v[1]
                    del new_coeffs[i]
                    del new_inps[i]
                    break
        return lin_inp(new_const, new_coeffs, new_inps)
    def __repr__(self):
        if not self.coeffs: return str(self.const)
        s = ' + '.join(f'{c}*{i}' if c != 1 else str(i) for c, i in zip(self.coeffs, self.inps))
        if self.const: s += f' + {self.const}'
        return s

def analyze(prev_z, index, a_list, b_list, c_list):
    if index == 14:
        if prev_z.const == 0:
            print(prev_z)
            return True
        return False
    z_mod_26_plus_b = prev_z.mod_26().add_const(b_list[index])
    next_inp = inp_range(index)
    next_inp_st_condition_false = z_mod_26_plus_b.overlap(next_inp)
    z_prev_div_a = prev_z.div_26() if a_list[index] == 26 else prev_z
    if next_inp_st_condition_false is None:
        # condition is not possible for all possible next_inp
        z = z_prev_div_a.times_26().add(1, next_inp).add_const(c_list[index])
        x = analyze(z, index + 1, a_list, b_list, c_list)
        if x:
            print(prev_z)
            return True
    else:
        # condition is possible for some next_inp
        # next_inp_st_condition_false represents the subset of next_inp that makes condition false
        z_condition_false = z_prev_div_a.times_26().add(1, next_inp_st_condition_false).add_const(c_list[index])
        z_condition_true = z_prev_div_a
        x = analyze(z_condition_false, index + 1, a_list, b_list, c_list)
        if x:
            print(f'# {next_inp_st_condition_false}')
            print(prev_z)
        y = analyze(z_condition_true, index + 1, a_list, b_list, c_list)
        if y:
            print(f'# not {next_inp_st_condition_false}')
            print(prev_z)
        assert not x or not y
        return x or y

analyze(lin_inp(0), 0, a_list, b_list, c_list)

'''
i4  = i3 - 8
i7  = i6 - 6 
i9  = i8 + 3 
i10 = i5 - 1
i11 = i2 - 5
i12 = i1 - 3
i13 = i0 + 7
'''
#           0  1  2  3  4  5  6  7  8  9 10 11 12 13
max_inps = [2, 9, 9, 9, 1, 9, 9, 3, 6, 9, 8, 4, 6, 9]

#           0  1  2  3  4  5  6  7  8  9 10 11 12 13
min_inps = [1, 4, 6, 9, 1, 2, 7, 1, 1, 4, 1, 1, 1, 8]

print()
min_inps_str = ''.join(str(i) for i in min_inps)
max_inps_str = ''.join(str(i) for i in max_inps)
print(f'{max_inps_str} -> {calc2(max_inps)}')
print(f'{min_inps_str} -> {calc2(min_inps)}')

quit()

print('z = 0')
li = lin_inp(0)

li_mod_26_plus_b = li.mod_26().add_const(b_list[0])
print('z % 26 + b[0] =', li_mod_26_plus_b)
i0 = inp_range(0)
print(f'overlap with {i0} is', li_mod_26_plus_b.overlap(i0), 'so condition is not possible')
z0 = (li if a_list[0] == 1 else li.div_26()).times_26().add(1, i0).add_const(c_list[0])
print('z =', z0)

z0_mod_26_plus_b = z0.mod_26().add_const(b_list[1])
print('z % 26 + b[1] =', z0_mod_26_plus_b)
i1 = inp_range(1)
print(f'overlap with {i1} is', z0_mod_26_plus_b.overlap(i1), 'so condition is not possible')
z1 = (z0 if a_list[1] == 1 else z0.div_26()).times_26().add(1, i1).add_const(c_list[1])
print('z =', z1)

z1_mod_26_plus_b = z1.mod_26().add_const(b_list[2])
print('z % 26 + b[2] =', z1_mod_26_plus_b)
i2 = inp_range(2)
print(f'overlap with {i2} is', z1_mod_26_plus_b.overlap(i2), 'so condition is not possible')
z2 = (z1 if a_list[2] == 1 else z1.idiv_26()).times_26().add(1, i2).add_const(c_list[2])
print('z =', z2)

z2_mod_26_plus_b = z2.mod_26().add_const(b_list[3])
print('z % 26 + b[3] =', z2_mod_26_plus_b)
i3 = inp_range(3)
print(f'overlap with {i3} is', z2_mod_26_plus_b.overlap(i3), 'so condition is not possible')
z3 = (z2 if a_list[3] == 1 else z2.div_26()).times_26().add(1, i3).add_const(c_list[3])
print('z =', z3)

z3_mod_26_plus_b = z3.mod_26().add_const(b_list[4])
print('z % 26 + b[4] =', z3_mod_26_plus_b)
i4 = inp_range(4)
overlap_with_i4 = z3_mod_26_plus_b.overlap(i4)
print(f'overlap with {i4} is', overlap_with_i4, 'so condition is possible')
z4t = (z3 if a_list[4] == 1 else z3.div_26())
z4f = (z3 if a_list[4] == 1 else z3.div_26()).times_26().add(1, overlap_with_i4[1]).add_const(c_list[4])
print('if true, z =', z4t)

z4t_mod_26_plus_b = z4t.mod_26().add_const(b_list[5])
print('z % 26 + b[5] =', z4t_mod_26_plus_b)
i5 = inp_range(5)
overlap_with_i5 = z4t_mod_26_plus_b.overlap(i5)
print(f'overlap with {i5} is', overlap_with_i5, 'so condition is not possible')
z5 = (z4t if a_list[5] == 1 else z4t.div_26()).times_26().add(1, i5).add_const(c_list[5])
print('z =', z5)


print()
print('if false, z =', z4f)


quit()

# 0: condition not possible, z = i0 + 9
# 1: condition not possible, z = 26*i0 + i1 + 235
# 2: condition not possible, z = 676*i0 + 26*i1 + i2 + 6121
# 3: condition not possible, z = 17576*i0 + 676*i1 + 26*i2 + i3 + 159149
# 4: condition possible iff i3 = 9 and i4 = 1, z = 676*i0 + 26*i1 + i2 + 6121
#     # 5: condition not possible, z = 17576*i0 + 676*i1 + 26*i2 + i5 + 159151
#     # 6: condition not possible, z = 456976*i0 + 17576*i1 + 676*i2 + 26*i5 + i6 + 4137926
#     # 7: condition possible iff i6 - 6 == i7
#           # 7: if i6 = 9 and i7 = 3, z = 17576*i0 + 676*i1 + 26*i2 + i5 + 159151
#                 # 8: condition not possible, z = 456976*i0 + 17576*i1 + 676*i2 + 26*i5 + i8 + 4137935
#                 # 9: condition possible iff i8 + 3 == i9
#                       # 9: if i8 = 1 and i9 = 4, z = 17576*i0 + 676*i1 + 26*i2 + i5 + 159151
#                             # 10: condition possible iff i5 - 1 == i10
#                                    ...
#                       # 9: if i8 = 2 and i9 = 5, z = ...
#                             # 10: pass
#                       # 9: if i8 = 3 and i9 = 6, z = ...
#                             # 10: pass
#                       # 9: if i8 = 4 and i9 = 7, z = ...
#                             # 10: pass
#                       # 9: if i8 = 5 and i9 = 8, z = ...
#                             # 10: pass
#                       # 9: if i8 = 6 and i9 = 9, z = ...
#                             # 10: pass
#                 # 9: condition false if not i8 + 3 == i9, z = ...
#                 # 10: pass
#           # 7: if i6 = 8 and i7 = 2, z = ...
#                 # 8: pass
#           # 7: if i6 = 7 and i7 = 1, z = ...
#                 # 8: pass
#     # 7: condition false if not i6 - 6 == i7, z = ...
#     # 8: pass
# 4: condition false if not (i3 = 9 and i4 = 1), z = ...
# 5: pass

while True:
    calc5([9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9])
    print(inps := [randint(1, 9) for _ in range(14)])
    calc5(inps)
print()
quit()

while True:
    inps = [randint(1, 9) for _ in range(14)]
    a = calc(code, inps[:])['z']
    b = calc2(inps[:])
    # c = regs['z'].eval(inps)
    c = calc3(inps[:])
    d = calc4(inps[:])
    e = calc5(inps[:])
    print(f'{inps} -> {a} {b} {c} {d} {e}')
    assert a == b == c == d == e
    if a == 0:
        assert False

quit()

print()
print('for i, a, b, c in vars:')
print('   x = 0')
print('   x = x + z_prev')
print('   x = x % 26')
print('   z = z_prev//a')
print('   x = x + b')
print('   x = x == i')
print('   x = x == 0')
print('   y = 0')
print('   y = y + 25')
print('   y = y*x')
print('   y = y + 1')
print('   z = z*y')
print('   y = 0')
print('   y = y + i')
print('   y = y + c')
print('   y = y*x')
print('   z = z + y')

print()
print('for i, a, b, c in vars:')
print('   x = z_prev % 26 + b != i')
print('   y = (i + c)*(z_prev % 26 + b != i)')
print('   z = (z_prev // a)*(25*(z_prev % 26 + b != i) + 1) + (i + c)*(z_prev % 26 + b != i)')

print()
print('for i, a, b, c in vars:')
print('   x = 0 if z_prev % 26 + b == i else 1')
print('   y = 0 if z_prev % 26 + b == i else i + c')
print('   z = (z_prev // a)*(25*(z_prev % 26 + b != i) + 1) + (i + c)*(z_prev % 26 + b != i)')

print()
print('for i, a, b, c in vars:')
print('   x = 0 if z_prev % 26 + b == i else 1')
print('   y = 0 if z_prev % 26 + b == i else i + c')
print('   z = (z_prev // a)*(1 if z_prev % 26 + b == i else 26) + (i + c)*(z_prev % 26 + b != i)')

print()
print('for i, a, b, c in vars:')
print('   x = 0 if z_prev % 26 + b == i else 1')
print('   y = 0 if z_prev % 26 + b == i else i + c')
print('   z = (z_prev // a) if z_prev % 26 + b == i else (z_prev // a)*26 + (i + c)*(z_prev % 26 + b != i)')

print()
print('for i, a, b, c in vars:')
print('   x = 0 if z_prev % 26 + b == i else 1')
print('   y = 0 if z_prev % 26 + b == i else i + c')
print('   z = (z // a if z_prev % 26 + b == i else (z_prev // a)*26) + (0 if z_prev % 26 + b == i else i + c)')

print()
print('for i, a, b, c in vars:')
print('   x = 0 if z % 26 + b == i else 1')
print('   y = 0 if z % 26 + b == i else i + c')
print('   z = (z//a if z % 26 + b == i else 26*(z//a) + i + c)')

print()
print('for i, a, b, c in vars:')
print('   z = z_prev//a')
print('   x = (z_prev % 26 + b) != i')
print('   y = 25*x + 1')
print('   z = z*y + y')
print('   y = (i + c)*x')

print()
print('for i, a, b, c in vars:')
print('   x = 1            if z_prev % 26 + b != i else 0')
print('   y = i + c        if z_prev % 26 + b != i else 0')
print('   z = 27*z_prev//a if z_prev % 26 + b != i else 2*z_prev//a')

print()
print('for i, a, b, c in vars:')
print('   if z_prev % 26 + b == i:')
print('      x, y, z = 0, 0,     2*z//a')
print('   else:')
print('      x, y, z = 1, i + c, 27*z_prev//a')

print()
print('for i, a, b, c in vars:')
print('   x = z_prev%26 + b != i')
print('   y = (i + c)*(z_prev%26 + b != i)')
print('   z = z_prev//a*(25*x + 1) + (i + c)*(z_prev%26 + b != i)')
