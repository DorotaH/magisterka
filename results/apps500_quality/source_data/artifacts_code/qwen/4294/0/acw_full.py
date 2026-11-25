import sys

# Read input from standard input
X, A = map(int, sys.stdin.readline().split())

# Determine the output based on the condition
if A > X:
	print(0)
else:
	print(10)
