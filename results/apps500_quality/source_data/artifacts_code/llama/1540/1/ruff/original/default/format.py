import sys

n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

log = []
for _ in range(k):
    log.append(tuple(map(int, input().split())))

d = [0] * n
for x, y in log:
    x -= 1
    y -= 1
    for i in range(n):
        if a[i][y]:
            d[i] += 1

print(*d)
