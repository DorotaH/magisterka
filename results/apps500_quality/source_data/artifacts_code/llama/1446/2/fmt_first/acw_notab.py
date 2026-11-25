import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def read_ints0():
    return map(lambda x: int(x) - 1, input().split())


def read_string():
    return input().strip()


def read_strings():
    return map(lambda s: s.strip(), input().split())


def make_graph(n, m):
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, x = read_ints0()
        graph[u].append((v, x))
        graph[v].append((u, x))
    return graph


def bfs(graph, k, types):
    dist = [k * [float("inf")] for _ in range(k)]
    for i in range(k):
        dist[i][i] = 0

    queue = [(0, 0)]
    while queue:
        d, u = queue.pop(0)
        for v, cost in graph[u]:
            if dist[v][i] > cost + d:
                dist[v][i] = cost + d
                queue.append((dist[v][i], v))

    return dist


n, m, k = read_ints()
c = list(read_ints())

types = [[] for _ in range(k)]
for i in range(k):
    types[i].extend(range(c[i], c[i] + c[i + 1]))

graph = make_graph(10**5, m)

dist = bfs(graph, k, 0)

if all(all(dist[i][j] != float("inf") for j in range(k)) for i in range(k)):
    print("Yes")
    for i in range(k):
        print(" ".join(map(str, dist[i])))
else:
    print("No")
