import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

castles = []
for i in range(n):
    a, b = int(data[3 + i * 3]), int(data[4 + i * 3])
    c = int(data[5 + i * 3])
    castles.append((a, b, c))

portals = defaultdict(list)
for i in range(m):
    u, v = int(data[3 + n * 3 + 2 * i]) - 1, int(data[3 + n * 3 + 2 * i + 1]) - 1
    portals[u].append(v)


def can_capture_all_castles():
    queue, visited = deque([0]), [False] * n
    visited[0] = True
    while queue:
        current = queue.popleft()
        for neighbor in portals[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return all(visited)


if not can_capture_all_castles():
    print(-1)
    sys.exit()


def max_defended_score():
    dp = [[0] * (k + 1) for _ in range(n)]
    dp[0][k] = 0
    for i in range(1, n):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if castles[i][0] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - castles[i][0]] + castles[i][2])
                for v in portals[i]:
                    if castles[i][0] <= j:
                        dp[i][j] = max(
                            dp[i][j],
                            dp[i - 1][j - castles[i][0]]
                            + castles[i][2]
                            + dp[v][j - castles[i][0]],
                        )
    return max(dp[n - 1])


print(max_defended_score())
