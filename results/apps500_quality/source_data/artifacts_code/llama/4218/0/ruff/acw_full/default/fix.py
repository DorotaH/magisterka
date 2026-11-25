import math


def solve(N):
	# Calculate the total number of possible integers not greater than N
	total_numbers = N
	# Calculate the number of odd integers not greater than N
	odd_numbers = math.floor(N / 2) + (N % 2)
	return odd_numbers / total_numbers


N = int(input())
ans = solve(N)
print(f"{ans:.10f}")
