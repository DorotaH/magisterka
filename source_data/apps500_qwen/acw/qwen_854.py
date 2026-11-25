import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Initialize the minimum number of moves to a large number
min_moves = float('inf')

# Iterate over possible values of i
for i in range(1, 1 + int(N**0.5)):
	if N % i == 0:
		# Calculate the corresponding j
		j = N // i
		# Calculate the number of moves needed to reach (i, j)
		moves = i + j - 2
		# Update the minimum number of moves if the current one is smaller
		min_moves = min(min_moves, moves)

# Print the minimum number of moves
print(min_moves)
