from collections import Counter


def restore_string(k, n, strings):
	# Count the frequency of each character in all strings
	char_count = Counter(''.join(strings))
	
	# Check if the total count of each character is even
	for char, count in char_count.items():
		if count % k != 0:
			return "-1"
	
	# Create a list to store the restored string
	restored_string = [''] * n
	
	# Iterate over each position in the string
	for i in range(n):
		# Collect characters from each string at position i
		chars = [s[i] for s in strings]
		# Sort the characters to find the original order
		sorted_chars = sorted(chars)
		# Place the characters in the restored string
		for j in range(k):
			restored_string[i] += sorted_chars[j]
	
	# Join the list into a single string and return
	return ''.join(restored_string)


# Read input
k, n = map(int, input().split())
strings = [input().strip() for _ in range(k)]

# Get the restored string
result = restore_string(k, n, strings)

# Print the result
print(result)
