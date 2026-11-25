import sys
from collections import defaultdict


def shortest_subsequence_to_square(n, a):
	# Dictionary to store the prime factorization of each number
	prime_factors = defaultdict(int)

	# Function to update the prime factorization
	def update_factors(num):
		factor = 2
		while factor**2 <= num:
			if num % factor == 0:
				prime_factors[factor] += 1
				num //= factor
			else:
				factor += 1
		if 1 < num:
			prime_factors[num] += 1

	# Function to check if a number is a perfect square
	def is_perfect_square():
		for count in prime_factors.values():
			if count % 2 != 0:
				return False
		return True

	# Iterate through the array to find the shortest subsequence
	start = 0
	end = 0
	min_length = float('inf')
	while end < n:
		update_factors(a[end])
		while is_perfect_square():
			min_length = min(min_length, end - start + 1)
			update_factors(a[start])
			start += 1
		end += 1

	if min_length == float('inf'):
		return -1
	return min_length


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(shortest_subsequence_to_square(n, a))
