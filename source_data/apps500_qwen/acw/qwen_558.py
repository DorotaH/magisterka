# Read input from standard input
A, B, C = map(int, input().split())

# Check if it's possible to make the sum congruent to C modulo B
if C % A == 0:
	print("YES")
else:
	print("NO")
