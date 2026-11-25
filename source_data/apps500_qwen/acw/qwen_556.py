# Read input from standard input
A, B, C = map(int, input().split())

# Check if the objective is achievable
if C % A == 0:
	print("YES")
else:
	print("NO")
