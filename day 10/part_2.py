pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {'(': 1, '[': 2, '{': 3, '<': 4}

def score(line):
	stack = []
	for c in line:
		if c in '([{<':
			stack.append(c)
		else:
			k = stack.pop()
			if pairs[k] != c:
				return None
	tot = 0
	for c in stack[::-1]:
		tot = tot*5 + scores[c]
	return tot

inp = ''.join(open('input.txt'))
lines = inp.split('\n')

scores = [score(line) for line in lines if score(line) is not None]
sorted_scores = sorted(scores)
mid = len(sorted_scores)//2
print(sorted_scores[mid])