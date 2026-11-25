from sys import stdin


def main():
    n, m, k = map(int, stdin.readline().split())
    c = list(map(int, stdin.readline().split()))
    inf = 10**15

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1
        return root_x == root_y

    edges = []
    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        edges.append((w, u, v))

    for i in range(1, k + 1):
        for j in range(c[i - 1] + 1, c[i] + 1):
            union(j, c[i - 1] + 1)

    for w, u, v in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v and union(u, v):
            print('No')
            return

    if find(1) != find(c[0] + 1):
        print('No')
        return

    d = [[inf] * k for _ in range(k)]
    for i in range(1, k + 1):
        d[i - 1][i - 1] = 0
        for j in range(i + 1, k + 1):
            for w, u, v in edges:
                root_u, root_v = find(u), find(v)
                if root_u == root_v and w >= 0:
                    d[i - 1][j - 1] = min(d[i - 1][j - 1], w)

    if any(all(x == inf for x in d[i])):
        print('No')
    else:
        print('Yes')
        for row in d:
            print(*row)

if __name__ == '__main__':
    main()
