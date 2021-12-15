from part_1 import evaluate

inp = ''.join(open('input.txt'))
poly, tail = inp.split('\n\n')

pairs = {k: v for k, v in (line.split(' -> ') for line in tail.split('\n'))}
counts = {c: poly.count(c) for c in set(poly)}

print(evaluate(poly, 40, pairs))