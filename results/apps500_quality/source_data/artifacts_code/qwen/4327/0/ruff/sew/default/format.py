import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the number of apples and pieces of apple
A, P = int(data[0]), int(data[1])

# Calculate the maximum number of apple pies
# We can use all pieces of apple and cut apples to get more pieces
total_pieces = (A * 3) + P
pies = total_pieces // 2

# Output the result
print(pies)
