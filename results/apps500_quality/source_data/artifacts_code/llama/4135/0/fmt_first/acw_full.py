def decrypt_string(n, s):
	"""
	Decrypts the string s by reversing substrings according to the given algorithm.

	Parameters:
	n (int): The length of the string.
	s (str): The encrypted string.

	Returns:
	str: The decrypted string.
	"""
	result = n * [""]  # Initialize the result list with empty strings
	for d in range(n, 0, -1):  # Iterate over divisors in decreasing order
		result[:n - d] = s[d - 1 : n][::-1]
		s = "".join(result)  # Update s for the next iteration
	return "".join(result)  # Return the decrypted string


# Read the input
n = int(input())
s = input().strip()  # Remove the newline character at the end

# Print the decrypted string
print(decrypt_string(n, s))
