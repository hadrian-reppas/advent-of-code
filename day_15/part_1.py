inp = ''.join(open('input.txt'))
nums = [[int(n) for n in line] for line in inp.split('\n')]

def add_edge(G, u, v, w, k):
    for _ in range(w - 1):
        G[u].add(k)
        G[k] = set()
        u = k
        k += 1
    G[u].add(v)
    return k

rows, cols = len(nums), len(nums[0])

G = {(i, j): set() for i in range(rows) for j in range(cols)}

k = 0
for i in range(rows):
    for j in range(cols):
        if i > 0:
            k = add_edge(G, (i, j), (i - 1, j), nums[i - 1][j], k)
        if j > 0:
            k = add_edge(G, (i, j), (i, j - 1), nums[i][j - 1], k)
        if i < rows - 1: # i < 5*rows - 1:
            k = add_edge(G, (i, j), (i + 1, j), nums[i + 1][j], k)
        if j < cols - 1: # j < 5*cols - 1:
            k = add_edge(G, (i, j), (i, j + 1), nums[i][j + 1], k)

def bfs(G, start, end):
    queue = [(start, 0)]
    visited = {start}
    while queue:
        v, w = queue.pop(0)
        for n in G[v]:
            if n in visited:
                continue
            if n == end:
                return w + 1
            visited.add(n)
            queue.append((n, w + 1))
    assert False

dist = bfs(G, (0, 0), (rows - 1, cols - 1))
print(dist)