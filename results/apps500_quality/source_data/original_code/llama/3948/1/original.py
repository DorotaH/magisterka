from collections import deque

def k_multihedgehog(n, edges, k):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the queue with the center vertex and its degree
    queue = deque([(1, 1)])
    parent = {1: None}
    while queue:
        node, degree = queue.popleft()
        for neighbor in graph[node]:
            if neighbor != parent.get(node, None):
                queue.append((neighbor, degree + 1))
                parent[neighbor] = node

    # Check if the graph is a k-multihedgehog
    if degree := parent[1] is not None:
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
    else:
        return "No"

    # Check if the graph is a tree
    for node in range(2, n + 1):
        if len(graph[node]) != 1:
            return "No"

    return "Yes"

# Read input from standard input
n, k = map(int, input().split())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Print the result to standard output
print(k_multihedgehog(n, edges, k))
