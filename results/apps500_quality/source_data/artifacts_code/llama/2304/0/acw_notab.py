import sys
input = sys.stdin.readline


class DisjointSet:
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
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
            self.parent[yr] = xr


def main():
    n, m = map(int, input().split())
    dsu = DisjointSet(1 + n)
    for _ in range(m):
        l, r, d = map(int, input().split())
        dsu.union(l, 1 + r)
        dsu.union(r, l + 1 + d)
    for i in range(1, 1 + n):
        if dsu.find(i) != dsu.find(1):
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
