def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def find_sequence_in_table(n, m, k, sequence):
	for i in range(1, 1 + n):
		current_gcd = gcd(i, 1)
		for j in range(2, 1 + m):
			current_gcd = gcd(current_gcd, j)
			if current_gcd == sequence[0]:
				found = all(gcd(i, l + j) == sequence[l] for l in range(1, k))
				if found:
					return "YES"
	return "NO"


# Read input
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Print output
print(find_sequence_in_table(n, m, k, sequence))
