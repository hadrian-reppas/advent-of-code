import networkx as nx

inp = ''.join(open('input.txt'))
nums = [[int(n) for n in line] for line in inp.split('\n')]

rows, cols = len(nums), len(nums[0])

def get(i, j):
    a, b = i//rows, j//cols
    m, n = i%rows, j%cols
    return (nums[m][n] - 1 + a + b)%9 + 1

G = nx.DiGraph()
for i in range(5*rows):
    for j in range(5*cols):
        if i > 0:
            G.add_edge((i, j), (i - 1, j), weight=get(i - 1, j))
        if j > 0:
            G.add_edge((i, j), (i, j - 1), weight=get(i, j - 1))
        if i < 5*rows - 1:
            G.add_edge((i, j), (i + 1, j), weight=get(i + 1, j))
        if j < 5*cols - 1:
            G.add_edge((i, j), (i, j + 1), weight=get(i, j + 1))

length = nx.algorithms.shortest_paths.astar.astar_path_length(G, (0, 0), (5*rows - 1, 5*cols - 1))
print(length)