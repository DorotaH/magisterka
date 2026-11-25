def is_k_multihedgehog(n, k, edges):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find the center of the hedgehog (a vertex with degree >= 3)
    center = None
    for vertex, degree in graph.items():
        if degree >= 3:
            center = vertex
            break

    if center is None:
        return "No"

    # Check if the rest of the graph is a valid (k-1)-multihedgehog
    visited, queue = set(), deque([center])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if len(graph[current]) == 1:
            # Remove the leaf vertex
            neighbor = graph[current][0]
            graph[current].remove(neighbor)
            graph[neighbor].remove(current)

            # Create a new hedgehog with center at the neighbor
            new_center = neighbor
            queue.append(new_center)
        elif len(graph[current]) > 1:
            # Check if the current vertex is connected to the center
            if center not in graph[current]:
                return "No"
            # Continue exploring the tree
            for neighbor in graph[current]:
                if neighbor != center:
                    queue.append(neighbor)

    # If all vertices are visited, it is a valid k-multihedgehog
    return "Yes" if len(visited) == n else "No"


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
edges = [(int(data[2 * i + 2]) - 1, int(data[2 * i + 3]) - 1) for i in range(n - 1)]

# Output the result
print(is_k_multihedgehog(n, k, edges))
