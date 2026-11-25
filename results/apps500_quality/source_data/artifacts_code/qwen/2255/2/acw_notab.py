from collections import defaultdict, deque


def lexicographically_smallest_sequence(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    for u in range(1, 1 + n):
        graph[u].sort()
    
    visited = [False] * (1 + n)
    visited[1] = True
    queue = deque([1])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result


# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = lexicographically_smallest_sequence(n, edges)

# Print the result
print(' '.join(map(str, result)))
