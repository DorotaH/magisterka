# Read input from standard input
K, X = map(int, input().split())

# Check if the sum of K coins is greater than or equal to X
if K * 500 >= X:
	print("Yes")
else:
	print("No")
