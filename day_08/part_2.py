from itertools import permutations

letters = 'abcdefg'
num_list = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
nums = {frozenset(num_list[n]): n for n in range(10)}

def get_mapping(left):
    for candidate_mapping in mappings():
        if valid_mapping(candidate_mapping, left):
            return candidate_mapping

def mappings():
    for perm in permutations(letters):
        yield {c: p for c, p in zip(letters, perm)}

def valid_mapping(mapping, left):
    return all(is_num(mapping, segs) for segs in left)
def is_num(mapping, segs):
    return frozenset(mapping[c] for c in segs) in nums

def get_val(mapping, right):
    return int(''.join(str(apply_mapping(mapping, segs)) for segs in right))
def apply_mapping(mapping, segs):
    return nums[frozenset(mapping[c] for c in segs)]

def decode(line):
    left, right = line
    mapping = get_mapping(left)
    return get_val(mapping, right)

inp = ''.join(open('input.txt'))
lines = [tuple(x.split(' ') for x in line.split(' | ')) for line in inp.split('\n')]

total = sum(decode(line) for line in lines)
print(total)