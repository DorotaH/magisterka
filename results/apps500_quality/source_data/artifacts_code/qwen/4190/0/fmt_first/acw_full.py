def min_lexicographical_c(n, a, b):
	# Sort array b based on the value of (a_i + b_i) % n
	b_sorted = sorted(b, key=lambda x: (a[b.index(x)], x))
	return [(b_sorted[i] + a[i]) % n for i in range(n)]


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

# Get the minimum lexicographical array c
c = min_lexicographical_c(n, a, b)

# Print the result
print(" ".join(map(str, c)))
