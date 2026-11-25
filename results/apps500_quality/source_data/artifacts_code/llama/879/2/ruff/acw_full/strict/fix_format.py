def find_path(n, p):
    graph = {i: [p[i - 1]] for i in range(2, 1 + n)}
    for i in range(2, n):
        graph[p[i - 1]].append(i + 1)

    visited = set()
    path = []

    def dfs(node, visited, path):
        visited.add(node)
        path.append(node)
        for child in graph[node]:
            if child not in visited:
                dfs(child, visited, path)

    dfs(1, visited, path)
    print(*path)


n = int(input())
p = list(map(int, input().split()))
find_path(n, p)
