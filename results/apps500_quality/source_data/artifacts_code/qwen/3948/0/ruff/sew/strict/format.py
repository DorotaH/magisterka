from collections import defaultdict, deque


def is_k_multihedgehog(n, k, edges):
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find the center of the hedgehog (node with degree >= 3)
    center = None
    for node, degree in graph.items():
        if degree >= 3:
            center = node
            break

    if center is None:
        return "No"

    # Perform BFS to check the structure of the graph
    visited, queue = set(), deque([center])
    visited.add(center)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Check if all vertices are visited and the structure is correct
    if len(visited) != n:
        return "No"

    # Check the degrees of the nodes
    for node, degree in graph.items():
        if node == center:
            if degree < 3:
                return "No"
        elif degree != 1:
            return "No"

    # Check the structure of the multihedgehog
    def is_multihedgehog(node, depth):
        if 1 == depth:
            return True
        for neighbor in graph[node]:
            if neighbor != center:
                if not is_multihedgehog(neighbor, depth - 1):
                    return False
        return True

    if not is_multihedgehog(center, k):
        return "No"

    return "Yes"


# Read input
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output result
print(is_k_multihedgehog(n, k, edges))
