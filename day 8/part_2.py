from itertools import permutations

letters = 'abcdefg'
num_list = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
nums = {frozenset(num_list[n]): n for n in range(10)}

def get_mapping(left):
    for candidate_mapping in map(make_mapping, permutations(letters)):
        if valid_mapping(candidate_mapping, left):
            return candidate_mapping

make_mapping = lambda vals: {c: v for c, v in zip(letters, vals)}
valid_mapping = lambda mapping, left: all(is_num(mapping, x) for x in left)
is_num = lambda mapping, x: frozenset(mapping[c] for c in x) in nums
get_val = lambda mapping, right: int(''.join(str(apply_mapping(mapping, x)) for x in right))
apply_mapping = lambda mapping, x: nums[frozenset(mapping[c] for c in x)]

def decode(left, right):
    mapping = get_mapping(left)
    return get_val(mapping, right)

inp = ''.join(open('input.txt'))
lines = [(line.split(' | ')[0].split(' '), line.split(' | ')[1].split(' ')) for line in inp.split('\n')]

print(sum(decode(left, right) for left, right in lines))