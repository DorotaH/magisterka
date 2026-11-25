def max_games(n):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 2 * (n // 2 - 1)
    else:
        return 2 * (n // 2)

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Get the number of players
n = int(data[0])

# Calculate and print the maximum number of games
print(max_games(n))
