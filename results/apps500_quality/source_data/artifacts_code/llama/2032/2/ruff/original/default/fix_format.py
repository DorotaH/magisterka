class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


def dijkstra(dist, n):
    for k in range(n):
        for u in range(n):
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + 1)


def main():
    n, m, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))

    d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][i] = a[i]

    e = [Edge(0, 0)]
    for _ in range(m):
        u, v = map(int, input().split())
        e.append(Edge(u, v))

    for i in range(len(e)):
        e[i].u -= 1
        e[i].v -= 1

    e.sort(key=lambda x: x.u)

    d1 = [0] * (n + 1)
    for i in range(1, n + 1):
        d1[i] = d[i][i] + b[i]

    for i in range(1, n + 1):
        dijkstra(d[i], n)

    f = [[-1] * (n + 1) for _ in range(n + 1)]
    f[0][0] = 0

    for i in range(1, n + 1):
        for j in range(n + 1):
            if d[i][j] == -1:
                continue
            f[i][j] = c[i]
            for k in range(i):
                f[i][j] = max(f[i][j], f[k][j] + c[i])

            for edge in e:
                if edge.u == i:
                    v = edge.v
                    if d[v][j + 1] != -1:
                        f[i][j] = max(f[i][j], f[i - 1][j + 1] + c[v])

        for j in range(1, n + 1):
            if d[i][j] == -1:
                break

    ans = -1
    for j in range(k, n + 1):
        if d[n][j] != -1:
            ans = max(ans, f[n][j])

    print(ans)


if __name__ == "__main__":
    main()
