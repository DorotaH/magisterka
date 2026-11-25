# Read input from standard input
K, X = map(int, input().split())

# Check if the sum of K coins is greater than or equal to X
if not K * 500 >= X:
    print("No")
else:
    print("Yes")