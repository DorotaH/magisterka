import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n - 2):
    a, b, c = map(int, input().split())
    q.append((a, b, c))

visited = [0] * (n + 1)
vis = [0] * (n + 1)
ans = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dq = deque()
        dq.append(i)
        visited[i] = 1
        while dq:
            x = dq.popleft()
            ans[x] = i
            for i in q:
                if x in i:
                    for j in i:
                        if not visited[j]:
                            dq.append(j)
                            visited[j] = 1
                            vis[j] = 1

for i in range(1, n + 1):
    if not vis[i]:
        dq = deque()
        dq.append(i)
        visited[i] = 1
        while dq:
            x = dq.popleft()
            ans[x] = i
            for i in q:
                if x in i:
                    for j in i:
                        if not visited[j]:
                            dq.append(j)
                            visited[j] = 1
                            vis[j] = 1

print(*ans[1:])
