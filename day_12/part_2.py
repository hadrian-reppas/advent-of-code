import networkx as nx

def count(G, v, counts):
    x = 0
    for n in G.neighbors(v):
        if n in ['start', 'end']:
            x += n == 'end'
        elif legal_visit(n, counts):
            x += count(G, n, counts)
            if n.islower():
                counts[n] -= 1
    return x

def legal_visit(n, counts):
    if n.isupper():
        return True
    if counts.get(n, 0) >= 1 and max(counts.values()) == 2:
        return False
    counts[n] = counts.get(n, 0) + 1
    return True

inp = ''.join(open('input.txt'))
edges = [line.split('-') for line in inp.split('\n')]

G = nx.Graph()
for u, v in edges:
    G.add_edge(u, v)

print(count(G, 'start', {}))