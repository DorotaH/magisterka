from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n - 2):
    a, b, c = map(int, input().split())
    q.append((a, b, c))

visited = [0] * (1 + n)
vis = [0] * (1 + n)
ans = [0] * (1 + n)

for i in range(1, 1 + n):
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

for i in range(1, 1 + n):
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
