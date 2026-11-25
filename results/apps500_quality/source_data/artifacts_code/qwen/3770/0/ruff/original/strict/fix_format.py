import sys
from collections import defaultdict


def max_profit(N, M, A, B, edges):
    # Create adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Function to calculate the score of a connected component
    def component_score(component):
        return abs(sum(B[i - 1] for i in component))

    # Function to calculate the profit of deleting a set of vertices
    def calculate_profit(deleted):
        score = 0
        for component in find_connected_components(graph, deleted):
            score += component_score(component)
        cost = sum(A[i - 1] for i in deleted)
        return score - cost

    # Function to find all connected components in the graph
    def find_connected_components(graph, deleted):
        visited = set()
        components = []
        for i in range(1, N + 1):
            if i not in visited and i not in deleted:
                component = set()
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        component.add(node)
                        for neighbor in graph[node]:
                            if neighbor not in visited and neighbor not in deleted:
                                stack.append(neighbor)
                components.append(component)
        return components

    # Brute force to find the maximum profit by trying all possible sets of deleted vertices
    max_profit = float("-inf")
    for r in range(1 << N):
        deleted = [i + 1 for i in range(N) if (r & (1 << i))]
        profit = calculate_profit(deleted)
        if profit > max_profit:
            max_profit = profit

    return max_profit


# Read input
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2 : 2 + N]))
B = list(map(int, data[2 + N : 2 + 2 * N]))
edges = []
for i in range(M):
    u = int(data[2 + 2 * N + 2 * i]) - 1
    v = int(data[2 + 2 * N + 2 * i + 1]) - 1
    edges.append((u, v))

# Calculate and print the maximum profit
print(max_profit(N, M, A, B, edges))
