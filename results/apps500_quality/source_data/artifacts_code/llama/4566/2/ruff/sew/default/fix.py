N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
roads = []

for _ in range(M):
    a, b=map(int, input().split())
    graph[a][b]+=1
    graph[b][a]+=1
    roads.append((a, b))

for i in range(1, 1+N):
    print(sum(graph[i][1:], 0))