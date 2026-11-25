# Function to calculate the number of ways to cover the belt-like area
def count_ways(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		# Using the recurrence relation: T(n) = T(n-1) + T(n-2)
		a, b = 1, 2
		for _ in range(3, 1 + n):
			a, b = b, a + b
		return b


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])
results = []

# Process each test case
for i in range(1, t + 1):
	n = int(data[i])
	results.append(count_ways(n))

# Output the results
for result in results:
	print(result)
