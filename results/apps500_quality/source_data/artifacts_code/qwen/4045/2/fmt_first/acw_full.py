def generate_string(n, s, t):
	if s == t:
		if s == "ab":
			return "NO"
		res = "a" * n + "b" * n + "c" * n
		return res + "YES\n" if s not in res else "NO"
	if s == "ab":
		if t == "bc":
			res = "cacb" * n
		elif t == "ca":
			res = "cabc" * n
		elif t == "ac":
			res = "abca" * n
		elif t == "cb":
			res = "acba" * n
	elif s == "bc":
		if t == "ab":
			res = "cacb" * n
		elif t == "ca":
			res = "cbac" * n
		elif t == "ac":
			res = "baca" * n
		elif t == "cb":
			res = "bacb" * n
	elif s == "ca":
		if t == "ab":
			res = "cacb" * n
		elif t == "bc":
			res = "cbac" * n
		elif t == "ac":
			res = "abac" * n
		elif t == "cb":
			res = "babc" * n

	return res + "YES\n" if s not in res and t not in res else "NO"


# Read input
n = int(input())
s = input()
t = input()

# Generate and print the result
result = generate_string(n, s, t)
print(result)
