import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
N = int(data[0])
R = int(data[1])

# Calculate the Inner Rating
inner_rating = R if N >= 10 else R + (10 - N) * 100
# Print the Inner Rating
print(inner_rating)
