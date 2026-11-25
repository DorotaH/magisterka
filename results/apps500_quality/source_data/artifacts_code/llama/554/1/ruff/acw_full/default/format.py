from sys import stdin
from collections import defaultdict


def solve():
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    subarrays = []
    for _ in range(m):
        l, r = map(int, stdin.readline().split())
        subarrays.append((l, r))

    freq = defaultdict(int)
    for sub in subarrays:
        freq[sub[0]] += 1
        freq[sub[1] + 1] -= 1

    happiness = 0
    count = 0
    for i in range(1, 1 + n):
        count += freq[i]
        happiness += a[i - 1] * count

    print(happiness)
