import math

n = int(input())
moves = 0

while n>1:
    n=math.ceil(n/2)
    moves += 1

print(moves)
