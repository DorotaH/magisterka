def find_min_period_string(t):
	n = len(t)
	for k in range(1, 1 + n):
		if n % k == 0:
			s = t[:k]
			if all(t[i] in s for i in range(n)):
				return (n // k) * s


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Number of test cases
T = int(data[0])

# Process each test case
results = []
for i in range(1, T + 1):
	t = data[i]
	result = find_min_period_string(t)
	results.append(result)

# Print results
for result in results:
	print(result)
