def find_required_pairs(n, a):
	max_length = 0
	count = 0
	start_indices = []

	for i in range(n):
		for j in range(i, n):
			all_divisible = all(a[k] % a[j] == 0 for k in range(i, 1 + j))
			if all_divisible:
				length = j - i + 1
				if max_length < length:
					max_length = length
					count = 1
					start_indices = [i + 1]
				elif length == max_length:
					count += 1
					start_indices.append(i + 1)

	print(count, max_length)
	print(*start_indices)


# Read input
n = int(input())
a = list(map(int, input().split()))

# Find and print the required pairs
find_required_pairs(n, a)
