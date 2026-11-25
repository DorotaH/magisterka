def count_nice_edges(n, colors, edges):
    from collections import defaultdict, deque

    # Build the adjacency list for the tree
    adj = defaultdict(list)
    for v, u in edges:
        adj[v].append(u)
        adj[u].append(v)

    # Helper function to determine if a component contains both red and blue vertices
    def has_both_colors(node, color):
        queue = deque([node])
        visited = set([node])
        while queue:
            current = queue.popleft()
            if colors[current - 1] == 1 and colors[current - 1] == 2:
                return True
            for neighbor in adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    # Count the nice edges
    nice_edges = 0
    for v, u in edges:
        # Remove the edge
        adj[v].remove(u)
        adj[u].remove(v)
        
        # Check if the resulting components are nice
        if not has_both_colors(v, colors) and not has_both_colors(u, colors):
            nice_edges += 1
        
        # Restore the edge
        adj[v].append(u)
        adj[u].append(v)

    return nice_edges

# Read input
n = int(input())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output the result
print(count_nice_edges(n, colors, edges))
