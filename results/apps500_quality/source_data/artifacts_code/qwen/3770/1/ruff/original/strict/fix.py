import sys
from collections import defaultdict


def max_profit(N, M, A, B, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, visited):
        stack = [node]
        component_sum = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                component_sum += B[node - 1]
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return abs(component_sum)

    max_profit = float('-inf')
    total_cost = sum(A)
    for i in range(1 << N):
        selected = [j for j in range(N) if (i & (1 << j))]
        visited = set()
        component_scores = []
        for node in selected:
            if node not in visited:
                component_scores.append(dfs(node + 1, visited))
        score = sum(component_scores)
        profit = score - sum(A[j] for j in selected)
        max_profit = max(max_profit, profit)

    return max_profit

# Read input
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:2+N]))
B = list(map(int, data[2+N:2+N+N]))
edges = []
for i in range(M):
    u = int(data[2+N+N+i*2]) - 1
    v = int(data[2+N+N+i*2+1]) - 1
    edges.append((u, v))

# Calculate and print the maximum profit
print(max_profit(N, M, A, B, edges))
