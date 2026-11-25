def max_games(n):
	return 2 * (n.bit_length() - 1)


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Get the number of players
n = int(data[0])

# Calculate and print the maximum number of games the winner can participate in
print(max_games(n))
