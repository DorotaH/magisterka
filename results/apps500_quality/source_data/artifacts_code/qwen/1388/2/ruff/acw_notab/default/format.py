def dfs(node, parent):
    if b[node] != c[node]:
        return -1 if a[node] == 0 else a[node]
    total_cost = 0
    for child in graph[node]:
        if child != parent:
            child_cost = dfs(child, node)
            if child_cost == -1:
                return -1
            total_cost += child_cost
    return total_cost


n = int(input())
a = [0] * (1 + n)
b = [0] * (1 + n)
c = [0] * (1 + n)
graph = [[] for _ in range(1 + n)]

for i in range(1, 1 + n):
    a[i], b[i], c[i] = map(int, input().split())

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = dfs(1, 0)
print(result)
