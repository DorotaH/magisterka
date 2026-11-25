def min_layers(N):
	return N * (N + 1) // 2


# Read input
N = int(input().strip())

# Output the result
print(min_layers(N))
