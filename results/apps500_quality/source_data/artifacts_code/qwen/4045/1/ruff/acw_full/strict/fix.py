def construct_string(n, s, t):
	if s == t:
		return "NO"

	# Check if s and t can be avoided by repeating a pattern
	pattern = "abc" * n
	if s in pattern or t in pattern:
		return "NO"

	res = "".join("abc" for _ in range(n))
	# Check if s and t are still in the result string
	return "NO" if s in res or t in res else res + "YES\n"


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
s = data[1]
t = data[2]

# Get result
result = construct_string(n, s, t)

# Print result
print(result)
