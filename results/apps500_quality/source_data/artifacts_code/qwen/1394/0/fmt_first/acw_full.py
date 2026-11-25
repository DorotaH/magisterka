def find_original_string(t):
	n = len(t)
	for i in range(n):
		if t[i] == "a":
			continue
		s = t[:i] + t[i + 1 :]
		s_prime = "".join([char for char in s if char != "a"])
		if s_prime + s == t:
			return s
	return ":("


# Read input
t = input().strip()

# Find and print the original string
result = find_original_string(t)
print(result)
