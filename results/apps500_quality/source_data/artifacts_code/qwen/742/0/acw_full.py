def find_minimal_permutation(n, b):
	from collections import defaultdict

	# Create a dictionary to store the positions of each element in b
	pos = defaultdict(list)
	for i, x in enumerate(b, start=1):
		pos[x].append(i)

	# Create a list to store the minimal permutation
	a = []

	# Iterate through the elements from 1 to 2n
	for x in range(1, 2 * n + 1):
		if pos[x]:
			# Get the smallest position of x in b
			i = pos[x].pop(0)
			# Add the smallest element and its partner to the permutation
			a.extend([x, 2 * n + 1 - x])

	# Check if the permutation is valid
	if len(a) != 2 * n:
		return -1

	return next((-1 for i in range(n) if b[i] != min(a[i * 2 - 1], a[i * 2])), a)


# Read input from standard input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
index = 1
results = []
for _ in range(t):
	n = int(data[index])
	b = list(map(int, data[1 + index:1 + index + n]))
	index += 1 + n
	result = find_minimal_permutation(n, b)
	results.append(result)

# Print the results
for result in results:
	if result == -1:
		print(-1)
	else:
		print(" ".join(map(str, result)))
