from collections import defaultdict
from sys import stdin

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

freq = defaultdict(int)
for num in seq:
    freq[num] += 1

moves = 0
for i in range(1, n + 1):
    moves += abs(freq[i] - 1)

print(moves)
