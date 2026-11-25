def kth_string(n, k):
	"""Return the k-th string of length n with n-2 'a' and 2 'b' in lexicographical order."""
	# Calculate the index of the first 'b' in the k-th string
	first_b_index = (k - 1) // (n - 2)

	# Calculate the number of 'a's to the left of the first 'b'
	a_count = first_b_index * (n - 2 - first_b_index)

	# Calculate the number of 'a's to the right of the first 'b'
	a_count_right = n - 2 - first_b_index - 1

	# Calculate the number of 'b's to the right of the first 'b'
	b_count_right = 2 - first_b_index % 2

	return (
		'a' * a_count
		+ 'b'
		+ 'a' * a_count_right
		+ 'b' * b_count_right
		+ 'a' * (n - a_count - a_count_right - b_count_right - 1)
	)


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
	# Read the values of n and k
	n, k = map(int, input().split())

	# Print the k-th string
	print(kth_string(n, k))
