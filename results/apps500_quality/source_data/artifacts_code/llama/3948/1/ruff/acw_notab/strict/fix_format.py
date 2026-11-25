from collections import deque


def k_multihedgehog(n, edges, k):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(1 + n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the queue with the center vertex and its degree
    queue = deque([(1, 1)])
    parent = {1: None}
    while queue:
        node, degree = queue.popleft()
        for neighbor in graph[node]:
            if neighbor != parent.get(node):
                queue.append((neighbor, degree + 1))
                parent[neighbor] = node

    if not (degree := parent[1] is not None):
        return "No"

    while degree <= k:
        queue.append((degree, 1))
        while queue:
            node, degree = queue.popleft()
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    queue.append((neighbor, degree + 1))
                    parent[neighbor] = node
        if degree != k:
            return "No"
    return next(("No" for node in range(2, 1 + n) if len(graph[node]) != 1), "Yes")


# Read input from standard input
n, k = map(int, input().split())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Print the result to standard output
print(k_multihedgehog(n, edges, k))
