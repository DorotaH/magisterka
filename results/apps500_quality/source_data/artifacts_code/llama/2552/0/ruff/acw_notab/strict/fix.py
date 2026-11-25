import sys

input = sys.stdin.readline


def dfs(graph, parent, node, n):
    parent[node] = -1
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                stack.append(neighbor)


def get_all_parents(graph, n):
    parent = [-1] * (1 + n)
    dfs(graph, parent, 1, n)
    return parent


def get_distance(graph, n):
    parent = get_all_parents(graph, n)
    distance = [0] * (1 + n)
    for i in range(2, 1 + n):
        distance[i] = distance[parent[i]] + 1
    return distance


def check_happiness(p, h, m, distance):
    n = len(p)
    delta = [0] * (1 + n)
    for i in range(1, 1 + n):
        delta[i] = h[i - 1] - p[i - 1] + p[0]
    for i in range(2, 1 + n):
        delta[parent[i]] += delta[i]
    for i in range(2, 1 + n):
        if (delta[i] % (2 * distance[i]) != 0 or delta[i] < 0):
            return False
        delta[parent[i]] += delta[i]
    return delta[1] == 0


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    h = list(map(int, input().split()))
    graph = [[] for _ in range(1 + n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    if check_happiness(p, h, m, get_distance(graph, n)):
        print("YES")
    else:
        print("NO")
