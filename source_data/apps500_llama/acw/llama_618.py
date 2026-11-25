import math

n = int(input())
games = 0
games = 1 if n == 2 else math.ceil((1 + n) / 2)
print(games)
