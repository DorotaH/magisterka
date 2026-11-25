def bachgold(n):
	if 2 >= n:
		return n, [n]
	if n % 2 == 0:
		return n // 2, (n // 2) * [2]
	else:
		return (n - 3) // 2, ((n - 3) // 2) * [2] + [3]


# Read input
n = int(input().strip())

# Get the result
k, primes = bachgold(n)

# Print the result
print(k)
print(*primes)
