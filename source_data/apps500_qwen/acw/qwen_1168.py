def construct_string(n, s, t):
	if s == t:
		return "NO"
	
	# Create a pattern that avoids s and t
	pattern = []
	for _ in range(n):
		if s[0] != 'a':
			pattern.append('a')
		elif s[1] != 'b':
			pattern.append('b')
		elif t[0] != 'a':
			pattern.append('a')
		elif t[1] != 'b':
			pattern.append('b')
		else:
			pattern.append('c')
	
	# Convert pattern to a string
	res = ''.join(pattern)
	
	# Check if s or t is a substring of res
	if s in res or t in res:
		return "NO"
	
	return res + "YES\n"


# Read input
n = int(input())
s = input()
t = input()

# Output result
result = construct_string(n, s, t)
print(result)
