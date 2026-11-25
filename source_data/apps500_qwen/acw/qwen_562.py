def kth_not_divisible(n, k):
	# The number of integers up to x that are divisible by n is x // n
	# Therefore, the k-th number not divisible by n is k + (k - 1) // (n - 1)
	return k + (k - 1) // (n - 1)


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
results = []
index = 1
for _ in range(t):
	n = int(data[index])
	k = int(data[1 + index])
	results.append(kth_not_divisible(n, k))
	index += 2

# Print results
for result in results:
	print(result)
