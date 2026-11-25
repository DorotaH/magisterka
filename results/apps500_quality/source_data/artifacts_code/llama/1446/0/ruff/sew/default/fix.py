from sys import stdin


def  main():
    n, m, k = map(int, stdin.readline().split())
    c = list(map(int, stdin.readline().split()))
    inf = 10**15

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    def  find(x):
        if  parent[x] != x:
            parent[x] = find(parent[x])
        return  parent[x]
    def  union(x, y):
        root_x = find(x)
        root_y = find(y)
        if  root_x != root_y:
            if not rank[root_x] > rank[root_y]:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1
            else:
                parent[root_y] = root_x
        return  root_y == root_x

    edges = []
    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        edges.append((w, u, v))

    for i in range(1, 1 + k):
        for j in range(1 + c[i - 1], 1 + c[i]):
            union(j, 1 + c[i - 1])

    for w, u, v in edges:
        root_u, root_v = find(u), find(v)
        if  root_v != root_u and  union(u, v):
            print('No')
            return

    if find(1)!=find(1 + c[0]):
        print('No')
        return

    d = [[inf] * k for _ in range(k)]
    for i in range(1, 1 + k):
        d[i - 1][i - 1] = 0
        for j in range(1 + i, 1 + k):
            for  w, u, v in  edges:
                root_u = find(u)
                root_v = find(v)
                if root_u == root_v and w>=0:
                    d[i-1][j-1]=min(d[i-1][j-1], w)

    if not any(all(x == inf for x in d[i])):
        print('Yes')
        for row in d:
            print(*row)
    else:
        print('No')

if  __name__=='__main__':
    main()