from collections import deque


class  UnionFind:
    def __init__(self, n):
        self.parent=list(range(0, n))
        self.rank=[0]*n

    def find(self, x):
        if  x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if  yr != xr:
            if  self.rank[yr] > self.rank[xr]:
                xr, yr = yr, xr
            elif  self.rank[yr] < self.rank[xr]:
                self.parent[yr] = xr
            else:
                self.parent[yr]=xr
                self.rank[xr]+=1


def main():
    n, e=map(int, input().split())
    uf, edges = UnionFind(n), []

    for  _ in  range(e):
        u, v=map(int, input().split())
        uf.union(u-1, v-1)
        edges.append((u-1, v-1))

    if n == 1 or uf.find(0) == 0:
        print("NO")
        return

    graph=[[] for  _ in  range(0, n)]
    for  u, v in  edges:
        graph[u].append(v)

    in_degree=[0]*n
    for  u in  range(n):
        for v in graph[u]:
            in_degree[uf.find(v)] += 1

    queue=deque([i for  i in  range(0, n) if  0 == in_degree[uf.find(i)]])

    while  queue:
        u=queue.popleft()
        for v in graph[u]:
            if  0 == in_degree[uf.find(v)]:
                continue
            in_degree[uf.find(v)] -= 1
            uf.union(u, v)
            if  0 == in_degree[uf.find(v)]:
                queue.append(v)

    if uf.find(0) == 0:
        print("YES")
        for  u, v in  edges:
            print(1+u, 1+uf.find(v))
        return

    print("NO")

if __name__ == "__main__":
    main()
