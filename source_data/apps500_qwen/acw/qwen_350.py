def min_changes_to_distinct_substrings(n, s):
	if 26 < n:
		return -1

	count = [0] * 26
	for char in s:
		count[ord(char) - ord('a')] += 1

	return sum(c - 1 for c in count if 1 < c)


# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(min_changes_to_distinct_substrings(n, s))
