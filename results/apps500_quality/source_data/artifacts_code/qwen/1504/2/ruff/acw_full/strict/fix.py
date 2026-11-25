import sys

input = sys.stdin.read
data = input().split()

# Read the number of test cases
t = int(data[0])

# Initialize index
index = 1
results = []

for _ in range(t):
	# Read the parameters for each test case
	n = int(data[index])
	k = int(data[1 + index])
	l1 = int(data[2 + index])
	r1 = int(data[3 + index])
	l2 = int(data[4 + index])
	r2 = int(data[5 + index])
	index += 6

	initial_intersection = sum(max(0, min(r1, r2) - max(l1, l2)) for _ in range(n))
	# Calculate the required additional intersection
	additional_intersection = k - initial_intersection

	# Calculate the minimum number of steps
	min_steps = 0
	if additional_intersection > 0:
		min_steps = additional_intersection

	# Append the result to the list
	results.append(min_steps)

# Print the results
print(*results, sep='\n')
