def  dfs(node, parent):
    if  b[node] != c[node]:
        if a[node] == 0:
            return -1
        else:
            return a[node]
    total_cost=0
    for  child in  graph[node]:
        if child != parent:
            child_cost=dfs(child, node)
            if  child_cost==-1:
                return  -1
            total_cost = total_cost + child_cost
    return total_cost


n=int(input())
a, b = [0] * (n + 1), [0] * (n + 1)
c, graph = [0] * (n + 1), [[] for _ in range(n + 1)]

for  i in  range(1, 1 + n):
    a[i], b[i], c[i] = map(int, input().split())

for  _ in  range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result=dfs(1, 0)
print(result)
