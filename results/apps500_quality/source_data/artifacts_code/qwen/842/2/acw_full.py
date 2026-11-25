def nth_even_length_palindrome(n):
	# Calculate the half-length of the palindrome
	half_length = (n - 1) // 2
	# Calculate the starting number for the half-length palindrome
	start = 10 ** half_length
	return int(str(start + n - 1) + str(start + n - 1)[::-1])


# Read the input
n = int(input().strip())

# Print the n-th even-length palindrome
print(nth_even_length_palindrome(n))
