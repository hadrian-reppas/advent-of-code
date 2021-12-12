def count(G, v, visited):
    x = 0
    for n in G[v]:
        if n == 'end':
            x += 1
        elif n not in visited:
            if v.islower():
                visited.add(v)
            x += count(G, n, visited)
            if v.islower():
                visited.remove(v)
    return x

inp = ''.join(open('input.txt'))
edges = [line.split('-') for line in inp.split('\n')]

G = {n: set() for n in sum(edges, [])}
for u, v in edges:
    G[u].add(v)
    G[v].add(u)

print(count(G, 'start', set()))