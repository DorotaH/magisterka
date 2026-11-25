def count_bonus_sales(n):
	# Define the range of numbers to check
	divisors = set(range(2, 11))

	return sum(bool(all(i % d != 0 for d in divisors)) for i in range(1, 1 + n))


# Read input
n = int(input())

# Output the result
print(count_bonus_sales(n))
