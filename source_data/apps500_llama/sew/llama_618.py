import math

n, games = int(input()), 0
if n == 2:
    games = 1
else:
    games = math.ceil((n + 1) / 2)

print(games)