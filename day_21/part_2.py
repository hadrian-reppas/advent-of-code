rolls = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

def step(counts, wins_1, wins_2):
    new_counts = {}
    for u, n in counts.items():
        old_pos_1, old_score_1, old_pos_2, old_score_2 = u
        for move_1, n_1 in rolls:
            for move_2, n_2 in rolls:
                pos_1 = (old_pos_1 + move_1 - 1)%10 + 1
                pos_2 = (old_pos_2 + move_2 - 1)%10 + 1
                score_1 = old_score_1 + pos_1
                score_2 = old_score_2 + pos_2
                if score_1 >= 21:
                    wins_1 += n*n_1*n_2
                elif score_2 >= 21:
                    wins_2 += n*n_1*n_2
                else:
                    new_universe = (pos_1, score_1, pos_2, score_2)
                    new_counts[new_universe] = new_counts.get(new_universe, 0) + n*n_1*n_2
    return new_counts, wins_1, wins_2

inp = ''.join(open('input.txt'))
pos_1, pos_2 = [int(line[28:]) for line in inp.split('\n')]

counts = {(pos_1, 0, pos_2, 0): 1}
wins_1 = wins_2 = 0

while counts:
    counts, wins_1, wins_2 = step(counts, wins_1, wins_2)

print(max(wins_1, wins_2)//27)