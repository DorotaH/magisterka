import sys
from collections import deque


def check(i, j, k, n, g, r, d, dist):
    q = deque([(0, i, k)])
    visited = {(i, j)}
    while q:
        time, x, y = q.popleft()
        if x == n:
            return True
        if y == g:
            for dx in range(-1, 2):
                nx, ny = dx + x, 0
                if 0 <= nx < n and (nx, ny) not in visited:
                    q.append((1 + time, nx, ny))
                    visited.add((nx, ny))
        if y < r:
            for dx in range(-1, 2):
                nx, ny = dx + x, y + 1
                if 0 <= nx < n and (nx, ny) not in visited and nx in d:
                    q.append((1 + time, nx, ny))
                    visited.add((nx, ny))
    return False


def solve():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    d.sort()
    inf = float("inf")
    dist = [[inf] * (1 + m) for _ in range(1 + n)]
    dist[0][0] = 0
    for i in range(1, m):
        for j in range(1, i):
            dist[d[i] - d[j]][i] = min(dist[d[i] - d[j]][i], g + dist[d[i]][j])

    for i in range(m):
        for j in range(i):
            for k in range(i + 1, m):
                if inf > dist[d[k] - d[i]][i] and inf > dist[d[k] - d[j]][j] and check(d[i], dist[d[i] - d[j]][j] + d[j], r, n, g, r, d, dist):
                    print(g + dist[d[i] - d[j]][j] + (n - d[i]) + d[k] - d[i] + 1)
                    return
    print(-1)


solve()
