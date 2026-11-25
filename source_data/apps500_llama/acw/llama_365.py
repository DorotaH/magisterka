x = int(input())


def min_steps(x):
	steps = [0] * (1 + x)
	for i in range(1, 1 + x):
		min_val = float('inf')
		for j in range(1, 1 + min(i, 5)):
			min_val = min(min_val, steps[i - j] + 1)
		steps[i] = min_val
	return steps[x]


print(min_steps(x))
