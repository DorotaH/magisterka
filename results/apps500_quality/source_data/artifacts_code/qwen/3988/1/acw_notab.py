from collections import defaultdict, deque


def max_reachable(graph, s):
    n = len(graph)
    visited = [False] * n
    visited[s - 1] = True
    queue = deque([s - 1])
    count = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                count += 1
                queue.append(neighbor - 1)
    return count


def min_reachable(graph, s):
    n = len(graph)
    visited = [False] * n
    visited[s - 1] = True
    queue = deque([s - 1])
    count = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                count += 1
                queue.append(neighbor - 1)
    return count


def orient_edges(n, m, s, edges):
    graph = defaultdict(list)
    for t, u, v in edges:
        graph[u - 1].append(v - 1)
        if t == 2:
            graph[v - 1].append(u - 1)
    max_reach = 0
    max_orient = []
    min_reach = float('inf')
    min_orient = []

    for i in range(m):
        new_graph = defaultdict(list)
        for j in range(m):
            if i == j:
                continue
            u, v = edges[j][:2]
            new_graph[u - 1].append(v - 1)
            new_graph[v - 1].append(u - 1)

        new_reach = max_reachable(new_graph, s)
        if new_reach > max_reach:
            max_reach = new_reach
            max_orient = ['+' if i != j else '-' for i in range(m) for j in range(m) if i != j]
        if new_reach < min_reach:
            min_reach = new_reach
            min_orient = ['+' if i != j else '-' for i in range(m) for j in range(m) if i != j]

    return max_reach, max_orient, min_reach, min_orient


n, m, s = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
max_reach, max_orient, min_reach, min_orient = orient_edges(n, m, s, edges)
print(max_reach)
print(''.join(max_orient))
print(min_reach)
print(''.join(min_orient))
