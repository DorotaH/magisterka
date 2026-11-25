import math


def count_divisors(n):
	"""Count the number of divisors for a given number."""
	return sum(
		1 if n / i == i else 2
		for i in range(1, int(math.sqrt(n)) + 1)
		if n % i == 0
	)


def shortest_subsequence_length(arr):
	"""Find the length of the shortest non-empty subsequence of arr product of whose elements is a perfect square."""
	n = len(arr)
	max_divisors = 7
	prime_factors = {}

	for num in arr:
		for i in range(2, int(math.sqrt(num)) + 1):
			while num % i == 0:
				if i in prime_factors:
					prime_factors[i] += 1
				else:
					prime_factors[i] = 1
				num //= i
		if num > 1:
			if num in prime_factors:
				prime_factors[num] += 1
			else:
				prime_factors[num] = 1

	shortest_length = float('inf')
	for i in range(1, 1 + n):
		count = 1
		for key in prime_factors:
			count *= (1 + prime_factors[key] // 2)
			if count > max_divisors:
				break
		if count <= max_divisors:
			shortest_length = min(shortest_length, i)

	return -1 if shortest_length == float('inf') else shortest_length


n = int(input())
arr = list(map(int, input().split()))
print(shortest_subsequence_length(arr))
