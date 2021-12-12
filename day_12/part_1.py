import networkx as nx

def count(G, v, visited):
    x = 0
    for n in G.neighbors(v):
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

G = nx.Graph()
for u, v in edges:
    G.add_edge(u, v)

print(count(G, 'start', set()))