from collections import defaultdict


def can_be_acyclic(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def has_cycle(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if has_cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    visited = [False] * (1 + n)
    rec_stack = [False] * (1 + n)

    # Check if the graph has a cycle without removing any edge
    if has_cycle(1, visited, rec_stack):
        return False

    # Try removing each edge and check if the graph becomes acyclic
    for u, v in edges:
        graph[u].remove(v)
        visited = [False] * (1 + n)
        rec_stack = [False] * (1 + n)
        if not has_cycle(1, visited, rec_stack):
            return True
        graph[u].append(v)

    return False


# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print("YES" if can_be_acyclic(n, edges) else "NO")
