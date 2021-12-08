inp = ''.join(open('aoc_3.txt'))

counts = [0]*12
n = 0

for line in inp.split('\n'):
    for i, c in enumerate(line):
        if int(c):
            counts[i] += 1
    n += 1

gamma_s = ''.join('1' if counts[i] > n - counts[i] else '0' for i in range(12))
gamma = int(gamma_s, 2)

epsilon_s = ''.join('0' if counts[i] > n - counts[i] else '1' for i in range(12))
epsilon = int(epsilon_s, 2)

print(gamma*epsilon)