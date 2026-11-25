def count_powerful_substrings(s):
	n = len(s)
	count = 0
	for i in range(n):
		if s[i:5 + i] == "heavy":
			for j in range(5 + i, 1 + n):
				if s[j - 5:j] == "metal":
					count += 1
	return count


# Read input
s = input().strip()

# Print the result
print(count_powerful_substrings(s))
