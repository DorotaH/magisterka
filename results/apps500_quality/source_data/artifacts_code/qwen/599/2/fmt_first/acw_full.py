def insert_to_make_palindrome(s):
	n = len(s)
	for i in range(n):
		# Try inserting a character at position i and check if the resulting string is a palindrome
		for char in "abcdefghijklmnopqrstuvwxyz":
			new_s = s[:i] + char + s[i:]
			if new_s == new_s[::-1]:
				return new_s
	return "NA"


# Read input
s = input().strip()

# Output the result
print(insert_to_make_palindrome(s))
