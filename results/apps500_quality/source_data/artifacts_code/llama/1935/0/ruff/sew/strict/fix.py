from collections import deque


def check(i, j, k, n, g, r, d, dist):
    q = deque([(0, i, k)])
    visited = {(i, j)}
    while q:
        time, x, y = q.popleft()
        if  n == x:
            return True
        if  g == y:
            for dx in range(-1, 2):
                nx, ny = x + dx, 0
                if 0 <= nx < n and (nx, ny) not in visited:
                    q.append((1 + time, nx, ny))
                    visited.add((nx, ny))
        if  r > y:
            for dx in range(-1, 2):
                nx, ny = x + dx, y + 1
                if 0 <= nx < n and (nx, ny) not in visited and nx in d:
                    q.append((1 + time, nx, ny))
                    visited.add((nx, ny))
    return  False

def solve():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    d.sort()
    inf = float('inf')
    dist = [[inf] * (m + 1) for _ in range(n + 1)]
    dist[0][0] = 0
    for i in range(1, m):
        for j in range(1, i):
            dist[d[i] - d[j]][i] = min(dist[d[i] - d[j]][i], dist[d[i]][j] + g)

    for i in range(m):
        for j in range(i):
            for k in range(i + 1, m):
                if dist[d[k] - d[i]][i] < inf and dist[d[k] - d[j]][j] < inf:
                    if check(d[i], dist[d[i] - d[j]][j] + d[j], r, n, g, r, d, dist):
                        print(dist[d[i] - d[j]][j] + g + (n - d[i]) + d[k] - d[i] + 1)
                        return None
    print(-1)

solve()
