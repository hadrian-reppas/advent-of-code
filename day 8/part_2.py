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

valid_mapping = lambda mapping, left: all(is_num(mapping, x) for x in left)
is_num = lambda mapping, x: frozenset(mapping[c] for c in x) in nums
get_val = lambda mapping, right: int(''.join(str(apply_mapping(mapping, x)) for x in right))
apply_mapping = lambda mapping, x: nums[frozenset(mapping[c] for c in x)]

def decode(line):
    left, right = line
    mapping = get_mapping(left)
    return get_val(mapping, right)

inp = ''.join(open('input.txt'))
lines = [tuple(x.split(' ') for x in line.split(' | ')) for line in inp.split('\n')]

total = sum(decode(line) for line in lines)
print(total)