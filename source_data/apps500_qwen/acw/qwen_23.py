def nth_even_length_palindrome(n):
	# Calculate the half-length of the palindrome
	half_length = 1 + (n - 1) // 2
	# Convert the half-length to a string
	half_str = str(half_length)
	# Create the palindrome by mirroring the half-length string
	palindrome = half_str + half_str[::-1]
	# If n is even, the palindrome is already even-length
	# If n is odd, we need to add a '0' in the middle
	return palindrome if n % 2 == 0 else '0' + palindrome[:-1] + palindrome[:-1]


# Read input
n = int(input().strip())
# Print the result
print(nth_even_length_palindrome(n))
