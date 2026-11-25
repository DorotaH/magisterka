import math

n = int(input())
games = 0
if n == 2:
    games = 1
else:
    games = math.ceil((n + 1) / 2)

print(games)
