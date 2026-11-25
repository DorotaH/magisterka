from collections import deque


def find_subgraph(N, M, edges):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append(v)

    # Use a queue for BFS, starting from vertices with an in-degree of 0
    queue = deque([i for i in range(1, N + 1) if len(graph[i]) == 0])
    visited = set()

    # Perform BFS
    while queue:
        u = queue.popleft()
        visited.add(u)
        for v in graph[u]:
            graph[v].remove(u)
            # If v has an in-degree of 0 and out-degree of 1, add it to the queue
            if len(graph[v]) == 1:
                queue.append(v)
                visited.add(v)
                graph[v].clear()

    # Check if all vertices have been visited
    if len(visited) < N:
        return -1

    # Print the subgraph
    print(len(visited))
    for u in visited:
        print(u)

# Read the input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Find and print the subgraph
find_subgraph(N, M, edges)
