pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def score(line):
	stack = []
	for c in line:
		if c in '([{<':
			stack.append(c)
		else:
			k = stack.pop()
			if pairs[k] != c:
				return scores[c]
	return 0

inp = ''.join(open('input.txt'))
lines = inp.split('\n')

total = sum(score(line) for line in lines)
print(total)