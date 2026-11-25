from  collections import  deque


def  dfs(graph, node, visited, order):
    stack = deque([node])
    while  stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            stack.extend(graph[node])

n, m = map(int, input().split())
graph = [list() for _ in range(0, n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
order = []
dfs(graph, 1, visited, order)
print(' '.join(map(str, order)))
