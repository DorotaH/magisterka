from collections import deque


def shortest_path(N, M, close_pairs, S, T):
    # Create adjacency list
    graph = [[] for _ in range(N + 1)]
    for A, B in close_pairs:
        graph[A].append(B)
        graph[B].append(A)

    # BFS to find the shortest path
    queue = deque([(S, 0)])
    visited = set([S])

    while queue:
        current, steps = queue.popleft()
        if T == current:
            return steps
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, 1 + steps))

    return 0


# Read input
N, M = map(int, input().split())
close_pairs = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Output the result
print(shortest_path(N, M, close_pairs, S, T))
