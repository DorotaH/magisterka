import sys

input=sys.stdin.readline

def  read_int():
    return int(input())

def  read_ints():
    return map(int, input().split())

def  read_ints0():
    return map(lambda x: int(x)-1, input().split())

def  read_string():
    return input().strip()

def  read_strings():
    return map(lambda s: s.strip(), input().split())

def  make_graph(n, m):
    graph = [list() for _ in range(n)]
    for _ in range(m):
        u, v, x = read_ints0()
        graph[u].append((v, x))
        graph[v].append((u, x))
    return graph

def  bfs(graph, k, types):
    dist = []
    for _ in range(k):
        dist.append([float("inf")] * k)
    for i in range(k):
        dist[i][i] = 0

    queue = [(0, 0)]
    while queue:
        d, u=queue.pop(0)
        for v, cost in graph[u]:
            if  dist[v][i]>d+cost:
                dist[v][i]=d+cost
                queue.append((dist[v][i], v))

    return dist


n, m, k=read_ints()
c=list(read_ints())

types=[list() for _ in range(0, k)]
for  i in  range(k):
    types[i].extend(range(c[i], c[i] + c[1 + i]))

graph=make_graph(10**5, m)

dist=bfs(graph, k, 0)

if all(all(dist[i][j] != float("inf") for j in range(k)) for i in range(k)):
    print("Yes")
    for i in range(k):
        print(" ".join(map(str, dist[i])))
else:
    print("No")