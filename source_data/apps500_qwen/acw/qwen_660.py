def min_electricity(n, a):
	return sum(
		a[i] * (2 * sum(abs(j - i) for j in range(n))) for i in range(n)
	)


# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the minimum electricity units
print(min_electricity(n, a))
