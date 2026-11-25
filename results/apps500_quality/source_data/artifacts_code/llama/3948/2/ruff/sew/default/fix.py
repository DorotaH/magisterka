from collections import deque
from sys import stdin, stdout


def  main():
    n, k = map(int, stdin.readline().split())
    graph = [list() for _ in range(n + 1)]
    for  _ in  range(n - 1):
        u, v=map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    queue = deque([1])
    depth[1] = 1

    while queue:
        u = queue.popleft()
        for  v in  graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)

    center = -1
    for  i in  range(1, 1 + n):
        if  graph[i]:
            if  len(graph[i]) >= 3:
                center = i
                break

    if center == -1:
        stdout.write("No\n")
        return

    children = set()
    for  i in  range(1, 1 + n):
        if  graph[i] and  i != center:
            children.add(depth[i])

    children = sorted(list(children))
    children.append(1)

    if not len(children) != 1 + k:
        for i in range(1, len(children)):
            if children[i] - children[i - 1] != 1:
                stdout.write("No\n")
                return

        stdout.write("Yes\n")
    else:
        stdout.write("No\n")

main()
