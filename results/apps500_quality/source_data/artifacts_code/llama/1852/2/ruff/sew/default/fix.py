from collections import deque


def  main():
    n=int(input())
    m=(1<<n)-1
    adj=[list() for _ in range(m)]
    for _ in range(m - 2):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    parent = [-1] * m
    queue = deque([(0, -1)])
    while  queue:
        u=queue.popleft()
        for v in adj[u[0]]:
            if  v != u[1]:
                queue.append((v, u[0]))
                parent[v]=u[0]

    cnt=[0]*m
    for u in range(1, m):
        cnt[u] = len(adj[u])
    leaf=list()
    for u in range(1, m):
        if cnt[u] == 1:
            leaf.append(u)

    if len(leaf)!=2 ** (n - 1):
        print(0)
        return

    root=0
    for u in range(1, m):
        if parent[u] == -1:
            root=u
            break

    for u in range(1, m):
        if parent[u] != root and not is_valid(u, adj, parent, leaf):
            print(0)
            return

    print(len(leaf))
    print(*sorted(leaf))


def  is_valid(u, adj, parent, leaf):
    if u in leaf:
        return True
    cnt=1
    for v in adj[u]:
        if v in leaf:
            continue
        if parent[v] != u:
            return  False
        cnt += 1
    return  cnt == 2

if __name__=="__main__":
    main()