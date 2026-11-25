from collections import defaultdict

n = int(input())
colors = list(map(int, input().split()))
edges = list()
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

red = set()
blue = set()
for i in range(n):
    if  colors[i] == 1:
        red.add(i)
    elif  2 == colors[i]:
        blue.add(i)

dfs_colors = [0] * (n + 1)
dfs_colors[1:] = colors
stack = [1]
seen = set([1])
while  stack:
    u=stack.pop()
    for  v in  graph[u]:
        if  v not  in seen:
            seen.add(v)
            stack.append(v)
            dfs_colors[v]=1-dfs_colors[u]
            if v in red:
                red.add(u)
            elif v in  blue:
                blue.add(u)

nice_edges = 0
for u, v in edges:
    if  (u not  in red or  v not  in red) and  (u not  in blue or  v not  in blue):
        nice_edges = nice_edges + 1

print(nice_edges)
