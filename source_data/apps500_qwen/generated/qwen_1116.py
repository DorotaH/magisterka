from collections import deque

def bfs_shortest_path(N, M, close_pairs, S, T):
    graph = [[] for _ in range(N + 1)]
    for A, B in close_pairs:
        graph[A].append(B)
        graph[B].append(A)
    
    queue = deque([(S, 0)])
    visited = [False] * (N + 1)
    visited[S] = True
    
    while queue:
        current, steps = queue.popleft()
        if current == T:
            return steps
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, steps + 1))
    
    return 0

# Read input
N, M = map(int, input().split())
close_pairs = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Output the result
print(bfs_shortest_path(N, M, close_pairs, S, T))
