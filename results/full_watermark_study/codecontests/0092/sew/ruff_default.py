n, m, k, r, c = map(int, input().split())
ax, ay, bx, by = map(int, input().split())
p = n * m
if ax != bx or ay != by:
    p -= c * r
print(pow(k, p, 1_000_000_007))
