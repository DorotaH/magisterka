def decrypt_string(t):
	n = len(t)
	s = t
	for d in range(n, 0, -1):
		s = s[d:] + s[:d][::-1]
	return s


# Read input
n = int(input().strip())
t = input().strip()

# Decrypt the string
s = decrypt_string(t)

# Print the result
print(s)
