import math

n = int(input())
moves = 0

while 1 < n:
    n = math.ceil(n / 2)
    moves += 1

print(moves)
