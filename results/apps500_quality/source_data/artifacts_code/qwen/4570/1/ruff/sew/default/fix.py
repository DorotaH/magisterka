import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
N, A = int(data[0]), int(data[1])
B = int(data[2])

# Calculate the minimum fee
min_fee = min(N * A, B)

# Print the minimum fee
print(min_fee)