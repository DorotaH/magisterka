import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Convert the input values to integers
x = list(map(int, data))

# Find the index of the variable that was assigned 0
index = x.index(0) + 1

# Print the index (1-based)
print(index)
