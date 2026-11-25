import sys

input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

degree = [0] * n
for i in range(n):
    for v in graph[i]:
        degree[i]+=1

q = [i for i in range(n) if degree[i] == 1]
q.sort(key=lambda x: w[x], reverse=True)

ans = []
while q:
    u = q.pop()
    ans.append(1 + u)
    for  v in  graph[u]:
        degree[v]-=1
        if  1 == degree[v]:
            q.append(v)
        elif  degree[v] == 0:
            print("DEAD")
            exit()

for i in range(n):
    if  degree[i] != 0:
        print("DEAD")
        exit()

print("ALIVE")
print(*ans)
