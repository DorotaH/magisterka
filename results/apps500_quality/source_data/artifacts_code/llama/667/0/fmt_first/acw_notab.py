import sys

N = int(sys.stdin.readline())

dist = [N * [float("inf")] for _ in range(N)]
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        dist[i][j] = row[j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[k][j] + dist[i][k])

print(max(max(row) for row in dist))
