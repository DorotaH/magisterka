def nth_even_length_palindrome(n):
	# The n-th even-length palindrome number is the same as the (n//2)-th odd-length palindrome number
	# plus 10^(n//2 - 1)
	return int(str(n // 2)[::-1] + str(n // 2))


# Read input
n = int(input().strip())

# Get the n-th even-length palindrome number
result = nth_even_length_palindrome(n)

# Print the result
print(result)
