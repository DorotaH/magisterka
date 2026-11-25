from collections import defaultdict


def maxProfit(N, M, A, B, edges):
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # DFS to find connected components
    visited = [False] * (N + 1)
    components = []
    for i in range(1, N + 1):
        if not visited[i]:
            component = []
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                component.append((A[node - 1], B[node - 1]))
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        visited[neighbor] = True
            components.append(component)

    # Calculate the maximum profit
    max_profit = float("-inf")
    for component in components:
        scores = [B[i] for A, B in component]
        score = abs(sum(scores))
        cost = sum(A for A, _ in component)
        max_profit = max(max_profit, score - cost)

    return max_profit


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

print(maxProfit(N, M, A, B, edges))
