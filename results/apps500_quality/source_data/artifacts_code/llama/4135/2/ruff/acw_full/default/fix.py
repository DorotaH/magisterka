def decrypt_string(n, t):
	"""
	Decrypts the given string t by reversing substrings according to the problem's algorithm.
	
	Args:
	n (int): The length of the string t.
	t (str): The encrypted string.
	
	Returns:
	str: The decrypted string.
	"""
	
	# Initialize an empty list to store the decrypted string
	s = [''] * n
	
	# Iterate over the divisors of n in decreasing order
	for d in range(n, 0, -1):
		# Reverse the substring s[1..d]
		s[:d] = t[-d:][::-1]
	
	# Join the list into a string and return it
	return ''.join(s)


# Read the input from standard input
n = int(input())
t = input()

# Print the decrypted string
print(decrypt_string(n, t))
