import sys


def compute_max_f():
	# Read the number of integers
	N = int(input())

	# Read the integers
	a = list(map(int, input().split()))

	# Sort the list in descending order
	a.sort(reverse=True)

	# Initialize max_f with 0
	max_f = 0

	# Compute the maximum value of f
	for m in range(N):
		f = sum((N - i) * a[i] * (a[m] // a[i]) for i in range(1 + m, N))
		max_f = max(max_f, f)

	# Print the maximum value of f
	print(max_f)


if __name__ == "__main__":
	compute_max_f()
