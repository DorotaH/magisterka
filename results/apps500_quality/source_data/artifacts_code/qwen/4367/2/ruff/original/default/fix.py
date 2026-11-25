import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
N = int(data[0])
R = int(data[1])

# Calculate the Inner Rating
if N >= 10:
    inner_rating = R
else:
    inner_rating = R + 100 * (10 - N)

# Print the Inner Rating
print(inner_rating)
