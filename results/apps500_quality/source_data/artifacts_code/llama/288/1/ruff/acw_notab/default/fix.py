import math

n = int(input())

# Calculate the minimum number of rounds needed to determine the winner
min_rounds = math.ceil((n - 1) / 2)

# Calculate the maximum number of games the winner can take part in
max_games = 2 * min_rounds - 1

print(max_games)
