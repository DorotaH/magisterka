def are_remainders_distinct(n, k):
	remainders = set()
	for i in range(1, k + 1):
		remainder = n % i
		if remainder in remainders:
			return "No"
		remainders.add(remainder)
	return "Yes"


# Read input
n, k = map(int, input().split())

# Print output
print(are_remainders_distinct(n, k))
