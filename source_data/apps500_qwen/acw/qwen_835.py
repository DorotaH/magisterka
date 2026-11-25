def max_prefixes(n, k, s, t):
	# The maximum number of unique prefixes is the length of the longest common prefix
	# between s and t. This is because any string that is a prefix of s or t and lies
	# within the range [s, t] will be counted in the result.
	max_prefix_length = 0
	for i in range(n):
		if s[i] == t[i]:
			max_prefix_length += 1
		else:
			break

	return 1 + max_prefix_length


# Read input from standard input
n, k = map(int, input().split())
s = input().strip()
t = input().strip()

# Print the result
print(max_prefixes(n, k, s, t))
