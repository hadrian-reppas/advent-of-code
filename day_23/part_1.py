from collections import deque

move_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def amphipod_locs(config):
    for j in range(7):
        if config[0][j] is not None: yield 0, j
    for i in range(1, len(config)):
        for j in range(4):
            if config[i][j] is not None: yield i, j

def room(amphi):
    return ord(amphi) - ord('A')

def enterable(config, index):
    for i in range(1, len(config)):
        if config[i][index] is None: continue
        if room(config[i][index]) != index:
            return False
    return True

def move(config, a, b, c, d):
    assert config[a][b] is not None
    assert config[c][d] is None
    new_config = []
    for i, row in enumerate(config):
        new_row = []
        for j, x in enumerate(row):
            if (i, j) == (a, b):
                new_row.append(None)
            elif (i, j) == (c, d):
                new_row.append(config[a][b])
            else:
                new_row.append(x)
        new_config.append(tuple(new_row))
    return tuple(new_config)

def get_moves(config, i, j):
    assert config[i][j] is not None
    amphi = config[i][j]
    if i == 0:
        # have to move into a room
        cost = 0
        for new_j in range(j, 1, -1):
            if new_j != j and config[0][new_j] is not None: break
            if new_j - 2 == room(amphi) and enterable(config, room(amphi)):
                room_cost = cost + move_cost[amphi]
                new_i = 1
                while new_i < len(config) and config[new_i][new_j - 2] is None:
                    new_i += 1
                    room_cost += move_cost[amphi]
                new_i -= 1
                yield (new_i, new_j - 2), room_cost
                return
            cost += move_cost[amphi]*(1 if new_j in [1, 6] else 2)
        cost = 0
        for new_j in range(j, 7):
            if new_j != j and config[0][new_j] is not None: break
            if new_j - 1 == room(amphi) and enterable(config, room(amphi)):
                room_cost = cost + move_cost[amphi]
                new_i = 1
                while new_i < len(config) and config[new_i][new_j - 1] is None:
                    new_i += 1
                    room_cost += move_cost[amphi]
                new_i -= 1
                yield (new_i, new_j - 1), room_cost
                return
            cost += move_cost[amphi]*(1 if new_j in [0, 5] else 2)
    else:
        if i > 1 and config[i - 1][j] is not None: return
        # have to move into the hallway and maybe a room
        to_hallway_cost = (i + 1)*move_cost[amphi]
        hallway_j = j + 1 # for looking left
        cost = to_hallway_cost
        for new_j in range(hallway_j, -1, -1):
            if config[0][new_j] is not None: break
            yield (0, new_j), cost
            if new_j - 2 == room(amphi) and enterable(config, room(amphi)):
                room_cost = cost + move_cost[amphi]
                new_i = 1
                while new_i < len(config) and config[new_i][new_j - 2] is None:
                    new_i += 1
                    room_cost += move_cost[amphi]
                new_i -= 1
                yield (new_i, new_j - 2), room_cost
            cost += move_cost[amphi]*(1 if new_j == 1 else 2)
        hallway_j = j + 2 # for looking right
        cost = to_hallway_cost
        for new_j in range(hallway_j, 7):
            if config[0][new_j] is not None: break
            yield (0, new_j), cost
            if new_j - 1 == room(amphi) and enterable(config, room(amphi)):
                room_cost = cost + move_cost[amphi]
                new_i = 1
                while new_i < len(config) and config[new_i][new_j - 1] is None:
                    new_i += 1
                    room_cost += move_cost[amphi]
                new_i -= 1
                yield (new_i, new_j - 1), room_cost
            cost += move_cost[amphi]*(1 if new_j == 5 else 2)

def get_all_moves(config):
    for i_i, j_i in amphipod_locs(config):
        for (i_f, j_f), cost in get_moves(config, i_i, j_i):
            yield (i_i, j_i), (i_f, j_f), cost

def search(starting_config, final):
    costs = {}
    stack = deque([(starting_config, 0)])
    while stack:
        config, cost = stack.popleft()
        if config in costs and costs[config] < cost: continue
        for (i_i, j_i), (i_f, j_f), move_cost in get_all_moves(config):
            new_config = move(config, i_i, j_i, i_f, j_f)
            new_cost = cost + move_cost
            if new_config in costs and new_cost >= costs[new_config]:
                continue
            costs[new_config] = new_cost
            stack.append((new_config, new_cost))
    return costs[final]

def main():
    inp = ''.join(open('input.txt'))
    starts = [[line[i] for i in range(3, 11, 2)] for line in inp.split('\n')[2:4]]
    config = ((None,)*7,) + tuple(tuple(row) for row in starts)

    final = ((None,)*7, ('A', 'B', 'C', 'D'), ('A', 'B', 'C', 'D')) 
    cost = search(config, final)

    print(cost)

if __name__ == '__main__':
    main()