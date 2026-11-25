def is_palindrome(s):
	"""Check if the given string is a palindrome."""
	return s == s[::-1]


def longest_non_palindrome(s):
	"""Find the length of the longest non-palindrome substring of the given string."""
	max_length = 0
	for i in range(len(s)):
		for j in range(i + 1, 1 + len(s)):
			substring = s[i:j]
			if not is_palindrome(substring) and max_length < j - i:
				max_length = j - i
	return max(max_length, 0)


# Read input from standard input
s = input().strip()

# Print the length of the longest non-palindrome substring
print(longest_non_palindrome(s))
