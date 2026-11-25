import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])

# Initialize the smallest x to a large number
smallest_x = float("inf")

# Iterate over possible values of x
for x in range(1, 10**6 + 1):
	if (x // k) * (x % k) == n:
		smallest_x = min(smallest_x, x)
		break

print(smallest_x)
