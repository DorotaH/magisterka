from collections import deque

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                xr, yr = yr, xr
            elif self.rank[xr] > self.rank[yr]:
                self.parent[yr] = xr
            else:
                self.parent[yr] = xr
                self.rank[xr] += 1

def main():
    n, e = map(int, input().split())
    uf = UnionFind(n)
    edges = []

    for _ in range(e):
        u, v = map(int, input().split())
        uf.union(u-1, v-1)
        edges.append((u-1, v-1))

    if n == 1 or uf.find(0) == 0:
        print("NO")
        return

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[uf.find(v)] += 1

    queue = deque([i for i in range(n) if in_degree[uf.find(i)] == 0])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if in_degree[uf.find(v)] == 0:
                continue
            in_degree[uf.find(v)] -= 1
            uf.union(u, v)
            if in_degree[uf.find(v)] == 0:
                queue.append(v)

    if uf.find(0) == 0:
        print("YES")
        for u, v in edges:
            print(u+1, uf.find(v)+1)
        return

    print("NO")

if __name__ == "__main__":
    main()
