from part_1 import search

inp = ''.join(open('input.txt'))
starts = [[line[i] for i in range(3, 11, 2)] for line in inp.split('\n')[2:4]]
config = ((None,)*7, tuple(starts[0]), ('D', 'C', 'B', 'A'), ('D', 'B', 'A', 'C'), tuple(starts[1]))

final = ((None,)*7, *4*(('A', 'B', 'C', 'D'),)) 
cost = search(config, final)

print(cost)