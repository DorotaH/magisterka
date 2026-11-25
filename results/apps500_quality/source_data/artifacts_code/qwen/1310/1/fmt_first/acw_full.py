def max_xor_segment(n, arr):
	max_xor = 0
	current_xor = 0
	prefix_xor = [0] * (1 + n)

	for i in range(n):
		current_xor ^= arr[i]
		max_xor = max(max_xor, current_xor)
		prefix_xor[i + 1] = current_xor

	for i in range(n):
		for j in range(i + 1, 1 + n):
			xor_value = prefix_xor[j] ^ prefix_xor[i]
			max_xor = max(max_xor, xor_value)

	return max_xor


# Read input
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(max_xor_segment(n, arr))
