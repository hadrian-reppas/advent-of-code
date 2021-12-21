rolls = 0
def roll():
    global rolls
    r = rolls % 100 + 1
    rolls += 1
    return r

def move(old, n):
    return (old + n - 1) % 10 + 1

inp = ''.join(open('input.txt'))
pos_1, pos_2 = [int(line[28:]) for line in inp.split('\n')]

score_1 = score_2 = 0

while True:
    pos_1 = move(pos_1, roll() + roll() + roll())
    score_1 += pos_1
    if score_1 >= 1000:
        break
    pos_2 = move(pos_2, roll() + roll() + roll())
    score_2 += pos_2
    if score_2 >= 1000:
        break

print(min(score_1, score_2)*rolls)