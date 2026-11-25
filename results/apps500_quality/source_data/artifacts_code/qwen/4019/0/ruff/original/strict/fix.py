from collections import defaultdict


def find_spanning_tree(n, m, D, edges):
    # Create adjacency list
    adj = defaultdict(list)
    for v, u in edges:
        adj[v].append(u)
        adj[u].append(v)

    # Check if it's possible to have a spanning tree with the required degree for vertex 1
    if len(adj[1]) < D:
        return "NO"

    # Remove edges to make vertex 1 have degree D
    edges_to_remove = []
    for v in adj[1]:
        if len(adj[v]) > 1:
            edges_to_remove.append((1, v))
            break

    for v, u in edges_to_remove:
        adj[v].remove(u)
        adj[u].remove(v)

    # Check if the remaining graph is connected
    visited = set()
    stack = [1]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for u in adj[v]:
                if u not in visited:
                    stack.append(u)

    if len(visited) == n:
        # Reconnect the removed edge if necessary
        if len(edges_to_remove) > 0:
            adj[1].append(edges_to_remove[0][1])
            adj[edges_to_remove[0][1]].append(1)
        return "YES\n" + "\n".join(f"{v} {u}" for v, u in edges_to_remove)
    else:
        return "NO"

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find and print the result
result = find_spanning_tree(n, m, D, edges)
print(result)
