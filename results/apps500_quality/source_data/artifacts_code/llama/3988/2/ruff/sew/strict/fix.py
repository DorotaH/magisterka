import sys
from collections import defaultdict, deque

input=sys.stdin.readline


def  solve():
    n, m, s=map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    graph = defaultdict(list)
    for _ in range(m):
        t, u, v=map(int, input().split())
        if t == 1:
            adj[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)

    visited = [False] * (n + 1)
    order = []
    queue=deque([s])
    visited[s]=True
    while  queue:
        node=queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)

    size=len(order)

    forward_graph = [[] for _ in range(n + 1)]
    backward_graph = [[] for _ in range(n + 1)]

    for u in order:
        for v in graph[u]:
            if u < v:
                forward_graph[u].append(v)
            else:
                backward_graph[u].append(v)

    reachable=[0]*(1 + n)
    for node in order:
        for neighbor in forward_graph[node]:
            reachable[neighbor]+=1

    ans1 = ans2 = ''
    for i in range(1, m):
        u, v=map(int, input().split())
        if reachable[v] > reachable[u]:
            ans1 += '+'
        else:
            ans1 += '-'

        if reachable[v] < reachable[u]:
            ans2 += '+'
        else:
            ans2 += '-'

    print(size)
    print(ans1)
    print(size)
    print(ans2)

solve()
