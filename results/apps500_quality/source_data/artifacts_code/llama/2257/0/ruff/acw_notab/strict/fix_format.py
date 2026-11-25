import math
import sys

input = sys.stdin.readline


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n, x1, y1, x2, y2 = map(int, input().split())
flowers = []
for _ in range(n):
    x, y = map(int, input().split())
    flowers.append((x, y))

min_val = 10**9
for r1 in range(int(1e7)):
    for r2 in range(int(1e7)):
        cover_all = True
        for flower in flowers:
            d1 = dist(x1, y1, flower[0], flower[1])
            d2 = dist(x2, y2, flower[0], flower[1])
            if d1 > r1 or d2 > r2:
                cover_all = False
                break
        if cover_all:
            min_val = min(min_val, r1**2 + r2**2)

print(min_val)
