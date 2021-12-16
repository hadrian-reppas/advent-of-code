def pop_int(stack, n):
    val = 0
    for _ in range(n):
        val <<= 1
        val |= stack.pop()
    return val

def parse(stack):
    version = pop_int(stack, 3)
    id = pop_int(stack, 3)
    match id:
        case 0:
            return parse_sum(stack)
        case 1:
            return parse_product(stack)
        case 2:
            return parse_minimum(stack)
        case 3:
            return parse_maximum(stack)
        case 4:
            return parse_literal(stack)
        case 5:
            return parse_greater_than(stack)
        case 6:
            return parse_less_than(stack)
        case 7:
            return parse_equal_to(stack)
        case _:
            assert False
    
def parse_literal(stack):
    val = 0
    while stack.pop():
        val <<= 4
        val += pop_int(stack, 4)
    val <<= 4
    val += pop_int(stack, 4)
    return val

def parse_args(stack):
    args = []
    l_id = stack.pop()
    if l_id:
        number = pop_int(stack, 11)
        for _ in range(number):
            args.append(parse(stack))
    else:
        length = pop_int(stack, 15)
        start_len = len(stack)
        while start_len - len(stack) < length:
            args.append(parse(stack))
        assert start_len - len(stack) == length
    return args

def parse_sum(stack):
    args = parse_args(stack)
    return sum(args)

def parse_product(stack):
    args = parse_args(stack)
    x = 1
    for arg in args:
        x *= arg
    return x

def parse_minimum(stack):
    args = parse_args(stack)
    return min(args)

def parse_maximum(stack):
    args = parse_args(stack)
    return max(args)

def parse_greater_than(stack):
    a, b = parse_args(stack)
    return int(a > b)

def parse_less_than(stack):
    a, b = parse_args(stack)
    return int(a < b)

def parse_equal_to(stack):
    a, b = parse_args(stack)
    return int(a == b)

inp, = open('input.txt')

bin = bin(int(inp, 16))[2:]
while len(bin) % 4 != 0:
    bin = '0' + bin

stack = []
for c in bin[::-1]:
    stack.append(c == '1')

print(parse(stack))