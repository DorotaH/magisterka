import sys
import math


def read_input():
    N, M, K = map(int, input().split())
    blasters = []
    for _ in range(K):
        r, c, t, f = map(int, input().split())
        blasters.append((r, c, t, f))
    return N, M, blasters


def distance(r1, c1, r2, c2):
    return max(abs(r1 - r2), abs(c1 - c2))


def check_time(t, blasters):
    return any(t >= start and (t - start) % freq == 0 for r, c, start, freq in blasters)


def dijkstra(N, M, blasters):
    d = {(i, j): float("inf") for i in range(1, N + 1) for j in range(1, 1 + M)}
    d[(1, 1)] = 0
    queue = [(0, (1, 1))]
    while queue:
        _, (r, c) = heapq.heappop(queue)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = dr + r, dc + c
            if (
                1 <= nr <= N
                and 1 <= nc <= M
                and d[nr, nc] > d[r, c] + 1
                and not check_time(d[r, c] + 1, blasters)
            ):
                d[nr, nc] = d[r, c] + 1
                heapq.heappush(queue, (d[nr, nc], (nr, nc)))
    return d.get((N, M), -1)


import heapq

N, M, blasters = read_input()
print("YES" if dijkstra(N, M, blasters) != -1 else "NO")
if dijkstra(N, M, blasters) != -1:
    print(dijkstra(N, M, blasters))
