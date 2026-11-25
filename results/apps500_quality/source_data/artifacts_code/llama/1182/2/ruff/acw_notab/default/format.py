import sys

r, c, n, k = map(int, input().split())

violins = []
for _ in range(n):
    x, y = map(int, input().split())
    violins.append((x, y))

count = 0
for top in range(1, 1 + r):
    for left in range(1, 1 + c):
        viola_count = sum(bool(top <= x <= r and left <= y <= c) for x, y in violins)
        if viola_count >= k:
            count += 1

print(count)
