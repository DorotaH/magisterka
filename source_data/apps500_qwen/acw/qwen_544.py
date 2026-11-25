import sys

# Read input from standard input
S = sys.stdin.readline().strip()

# Initialize the minimum difference to a large number
min_diff = float('inf')

# Iterate over all possible starting positions for the three consecutive digits
for i in range(len(S) - 2):
	# Extract the three consecutive digits
	X = int(S[i:i + 3])
	# Calculate the absolute difference between X and 753
	diff = abs(X - 753)
	# Update the minimum difference if the current one is smaller
	if diff < min_diff:
		min_diff = diff

# Print the minimum possible difference
print(min_diff)
