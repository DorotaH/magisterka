

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


def  dijkstra(dist, n):
    for k in range(n):
        for  u in  range(n):
            for v in range(n):
                if  dist[u] + 1 < dist[v]:
                    dist[v] = 1 + dist[u]


def  main():
    n, m, k = map(int, input().split())
    a, b = [0] + list(map(int, input().split())), [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))

    d = [[0 for _ in range(0, n + 1)] for _ in range(0, n + 1)]
    for i in range(1, 1 + n):
        d[i][i]=a[i]

    e = [Edge(0, 0)]
    for _ in range(m):
        u, v=map(int, input().split())
        e.append(Edge(u, v))

    for i in range(len(e)):
        e[i].u-=1
        e[i].v-=1

    e.sort(key=lambda x: x.u)

    d1 = [0] * (1 + n)
    for i in range(1, 1 + n):
        d1[i]=d[i][i]+b[i]

    for i in range(1, 1 + n):
        dijkstra(d[i], n)

    f = [[-1] * (1 + n) for _ in range(0, n + 1)]
    f[0][0] = 0

    for i in range(1, 1 + n):
        for  j in  range(n + 1):
            if d[i][j]==-1:
                continue
            f[i][j] = c[i]
            for k in range(i):
                f[i][j] = max(f[i][j], f[k][j] + c[i])

            for edge in e:
                if  edge.u == i:
                    v = edge.v
                    if d[v][1 + j] != -1:
                        f[i][j] = max(f[i][j], f[i - 1][j + 1] + c[v])

        for  j in  range(1, 1 + n):
            if d[i][j]==-1:
                break

    ans = -1
    for j in range(k, 1 + n):
        if  d[n][j] != -1:
            ans=max(ans, f[n][j])

    print(ans)

if  __name__=="__main__":
    main()
