import math
import sys

N = int(input())
N += 1
moves = 0
while True:
    moves += 1
    if math.sqrt(N) - int(math.sqrt(N)) == 0:
        break
    N += 1
print(moves)
