import sys

n, m = map(int, input().split())
visitors = []
for _ in range(0, m):
    l, r = map(int, input().split())
    visitors.append((l - 1, r))

visitors.sort(key=lambda x: x[0])
s, prefix_sum = [0] * n, 0
for l, r in visitors:
    best = 0
    best_pos = 0
    for pos in range(l, r):
        if s[pos] == 0:
            beauty = (r - l + 1) * (pos - l + 1)
            if beauty > best:
                best = beauty
                best_pos = pos
    s[l:r] = [1] * (r - l + 1)
    s[best_pos] = 0

print("".join(map(str, s)))
