def pop_int(stack, n):
    val = 0
    for _ in range(n):
        val <<= 1
        val |= stack.pop()
    return val

def parse(stack):
    version = pop_int(stack, 3)
    versions.append(version)
    id = pop_int(stack, 3)
    if id == 4:
        parse_literal(stack)
    else:
        parse_operator(stack)
    
def parse_literal(stack):
    val = 0
    while stack.pop():
        val <<= 4
        val += pop_int(stack, 4)
    val <<= 4
    val += pop_int(stack, 4)
    return val

def parse_operator(stack):
    if stack.pop():
        number = pop_int(stack, 11)
        for _ in range(number):
            parse(stack)
    else:
        length = pop_int(stack, 15)
        start_len = len(stack)
        while start_len - len(stack) < length:
            parse(stack)
        assert start_len - len(stack) == length

inp, = open('input.txt')

bin = bin(int(inp, 16))[2:]

stack = []
for c in bin[::-1]:
    stack.append(c == '1')
while len(stack) % 4 != 0:
    stack.append(False)

versions = []

parse(stack)

print(sum(versions))