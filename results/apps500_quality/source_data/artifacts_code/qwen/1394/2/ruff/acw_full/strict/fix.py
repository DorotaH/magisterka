def find_s(t):
	n = len(t)
	for i in range(n // 2 + 1):
		s = t[:i]
		s_prime = t[i:].replace('a', '')
		if s_prime + s == t:
			return s
	return ":("


# Read input from standard input
t = input().strip()

# Find and print the result
result = find_s(t)
print(result)
