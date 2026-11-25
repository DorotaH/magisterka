from collections import deque


def bfs(root, parent, graph, visited):
    q = deque()
    q.append(root)
    visited[root] = True
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor != parent and not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True


def dfs(node, parent, graph, visited):
    for neighbor in graph[node]:
        if neighbor != parent and not visited[neighbor]:
            dfs(neighbor, node, graph, visited)


def construct_spanning_tree(graph, n, m, D):
    visited = [False] * (1 + n)
    graph = [[0] * (1 + n) for _ in range(1 + n)]
    for i in range(1, 1 + n):
        graph[i][i] = 0
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    if D == 1:
        return "YES\n" + "\n".join(f"{i} {1}" for i in range(2, 1 + n))

    for i in range(1, 1 + n):
        if graph[1][i] and visited[i]:
            continue

        bfs(i, 1, graph, visited)

        if visited[1] and sum(graph[1]) == D:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, 1 + n))
        elif visited[1] and D < sum(graph[1]):
            return "NO"

    return "NO"


n, m, D = map(int, input().split())
print(construct_spanning_tree(graph, n, m, D))
