import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
N, A = int(data[0]), int(data[1])
B = int(data[2])

# Calculate the minimum total travel expense
min_cost = min(N * A, B)

# Print the result
print(min_cost)
