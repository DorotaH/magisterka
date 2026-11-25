import sys


def max_f(N, a):
	max_val = 0
	for m in range(1, max(a) * 2 + 1):
		current_val = sum(m % ai for ai in a)
		if current_val > max_val:
			max_val = current_val
	return max_val


# Read input
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# Calculate and print the result
print(max_f(N, a))
