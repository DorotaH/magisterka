import sys

n = int(input())

w = []
h = []
for _ in range(n):
    w_i, h_i = map(int, input().split())
    w.append(w_i)
    h.append(h_i)

min_area = float("inf")
for i in range(2**n):
    area = 0
    used = [0] * n
    for j in range(n):
        bit = i >> j & 1
        area += h[j] * w[j]
        used[j] = 1 if bit else -1
    max_h = max(h[i] if used[i] == 1 else w[i] for i in range(n))
    area += (sum(w[i] if used[i] == -1 else h[i] for i in range(n)) - max_h) * max_h
    min_area = min(min_area, area)

print(min_area)
