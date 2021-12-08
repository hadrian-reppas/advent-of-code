inp = ''.join(open('aoc_3.txt'))
lines = inp.split('\n')

bit = 0
while len(lines) > 1:
    count = 0
    for line in lines:
        count += line[bit] == '1'
    common = '1' if count >= len(lines) - count else '0'
    lines = [line for line in lines if line[bit] == common]
    bit += 1

oxygen = int(lines[0], 2)

lines = inp.split('\n')

bit = 0
while len(lines) > 1:
    count = 0
    for line in lines:
        count += line[bit] == '1'
    uncommon = '1' if count < len(lines) - count else '0'
    lines = [line for line in lines if line[bit] == uncommon]
    bit += 1

CO2 = int(lines[0], 2)

print(oxygen*CO2)