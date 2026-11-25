# Read input
a, b = map(int, input().split())

# Initialize variables
score = 0
result = []

# Determine the maximum score and arrangement
if a > b:
	score = sum((i + 1) ** 2 for i in range(b))
	result = ['o'] * b + (a - b) * ['x']
elif a < b:
	score = -sum((i + 1) ** 2 for i in range(a))
	result = a * ['x'] + ['o'] * (b - a)
else:
	score = 0
	result = a * ['o'] + b * ['x']

# Output the result
print(score)
print(''.join(result))
