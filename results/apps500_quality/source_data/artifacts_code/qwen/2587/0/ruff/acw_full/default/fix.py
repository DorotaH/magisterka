def find_min_x(n):
	# If n is 1, the only digit is 8 which gives the maximum possible r
	return 8 if n == 1 else int('1' + '9' * (n - 1))


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])

# Process each test case
results = []
for i in range(1, t + 1):
	n = int(data[i])
	results.append(find_min_x(n))

# Print results
for result in results:
	print(result)
