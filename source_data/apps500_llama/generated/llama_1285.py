from collections import deque

def find_subgraph():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    match = [-1] * (n + 1)
    for i in range(1, n + 1):
        if graph[i]:
            queue = deque([i])
            while queue:
                v = queue.popleft()
                if match[v] != -1:
                    continue
                for u in graph[v]:
                    if match[u] == -1:
                        match[u] = v
                        match[v] = u
                        queue.append(u)
                    elif match[match[u]] == v:
                        match[u] = v
                        match[v] = u

    subgraph = [i for i in range(1, n + 1) if match[i] != -1]
    if len(subgraph) == 0:
        print(-1)
    else:
        print(len(subgraph))
        print(*subgraph)

find_subgraph()
