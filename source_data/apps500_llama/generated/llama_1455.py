from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))
    edges.append((v-1, u-1))

adj = [[] for _ in range(N)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * N
stack = []
for i in range(N):
    if not visited[i]:
        stack.append(i)
        visited[i] = True
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

total = 0
for i in range(N):
    total += B[i]

max_profit = 0
visited = [False] * N
stack = []
for i in range(N):
    if not visited[i]:
        stack.append(i)
        visited[i] = True
        total_component = 0
        total_cost = 0
        while stack:
            node = stack.pop()
            total_component += B[node]
            total_cost += A[node]
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        max_profit = max(max_profit, abs(total_component) - total_cost)

print(max_profit)
