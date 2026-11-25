import sys

N, M, K = map(int, input().split())
grid = [[0] * (M + 1) for _ in range(N + 1)]
blasters = []
times = []

for _ in range(K):
    x, y, t, f = map(int, input().split())
    blasters.append((x, y, t, f))
    times.append(t)

max_time = 3000
dist = [[max_time] * (M + 1) for _ in range(N + 1)]
dist[1][1] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        for x, y, t, f in blasters:
            cur_time = t + (dist[i][j] - t) // f * f
            if cur_time >= t + f and cur_time < max_time:
                if x - 1 == j and i > 1 and cur_time + i - 1 < dist[i - 1][j]:
                    dist[i - 1][j] = cur_time + i - 1
                if y - 1 == i and j > 1 and cur_time + j - 1 < dist[i][j - 1]:
                    dist[i][j - 1] = cur_time + j - 1
                if x + 1 == j and cur_time + N - i < dist[i + 1][j]:
                    dist[i + 1][j] = cur_time + N - i
                if y + 1 == i and cur_time + M - j < dist[i][j + 1]:
                    dist[i][j + 1] = cur_time + M - j

if dist[N][M] == max_time:
    print("NO")
else:
    print("YES")
    print(dist[N][M])
