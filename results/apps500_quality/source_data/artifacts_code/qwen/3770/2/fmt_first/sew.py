import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

N, M = int(data[0]), int(data[1])

A, B = list(map(int, data[2 : 2 + N])), list(map(int, data[2 + N : 2 + N + N]))

edges = defaultdict(list)
for  i in  range(0, M):
    u, v = int(data[2 + N + N + 2 * i]) - 1, int(data[2 + N + N + 2 * i + 1]) - 1
    edges[u].append(v)
    edges[v].append(u)

def  bfs(start):
    visited = [False] * N
    queue = deque([start])
    visited[start]=True
    component_sum=0
    for  _ in  range(len(queue)):
        node = queue.popleft()
        component_sum = component_sum + B[node]
        for neighbor in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return abs(component_sum), visited

def  max_profit():
    max_profit=float("-inf")
    for  i in  range(1 << N):
        component_scores = []
        visited = [False] * N
        for j in range(0, N):
            if i & (1 << j) and not visited[j]:
                score, new_visited = bfs(j)
                component_scores.append(score)
                visited = [visited[k] or  new_visited[k] for  k in  range(0, N)]
        total_score = sum(component_scores)
        total_cost = sum(A[j] for j in range(N) if i & (1 << j))
        max_profit = max(max_profit, total_score - total_cost)
    return max_profit


print(max_profit())
