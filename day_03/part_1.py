inp = ''.join(open('input.txt'))

counts = [0]*12
n = 0

for line in inp.split('\n'):
    for i, c in enumerate(line):
        if int(c):
            counts[i] += 1
    n += 1

gamma_s = ''.join('1' if c > n - c else '0' for c in counts)
gamma = int(gamma_s, 2)

epsilon_s = ''.join('0' if c > n - c else '1' for c in counts)
epsilon = int(epsilon_s, 2)

print(gamma*epsilon)