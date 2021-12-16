def apply(a, b, n, pairs):
    if (a, b, n) in cache:
        return cache[(a, b, n)]
    elif n == 1:
        if a + b not in pairs:
            return {}
        x = {pairs[a + b]: 1}
        cache[(a, b, n)] = x
        return x
    else:
        if a + b not in pairs:
            return {}
        c = pairs[a + b]
        x = combine(apply(a, c, n - 1, pairs), 
                    apply(c, b, n - 1, pairs))
        x[c] = x.get(c, 0) + 1
        cache[(a, b, n)] = x
        return x

def combine(a, b):
    return {c: a.get(c, 0) + b.get(c, 0) for c in a | b}

def evaluate(poly, n, pairs):
    slow, fast = iter(poly), iter(poly)
    next(fast)
    counts = {c: poly.count(c) for c in set(poly)}
    for a, b in zip(slow, fast):
        counts = combine(counts, apply(a, b, n, pairs))
    low, *_, high = sorted(counts.values())
    return high - low

cache = {}
pairs = {}

def main():
    inp = ''.join(open('input.txt'))
    poly, tail = inp.split('\n\n')

    pairs = {k: v for k, v in (line.split(' -> ') for line in tail.split('\n'))}
    counts = {c: poly.count(c) for c in set(poly)}

    diff = evaluate(poly, 10, pairs)
    print(diff)

if __name__ == '__main__':
    main()