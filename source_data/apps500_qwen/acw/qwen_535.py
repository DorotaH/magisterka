import sys
import math


def main():
	# Read input from standard input
	input = sys.stdin.read
	data = input().split()

	# Convert input data to integers
	A = [int(x) for x in data]

	# Sort the array to find the minimum cost
	A.sort()

	min_cost = sum(abs(A[i] - A[i - 1]) for i in range(1, len(A)))
	# Print the minimum cost
	print(min_cost)


if __name__ == "__main__":
	main()
