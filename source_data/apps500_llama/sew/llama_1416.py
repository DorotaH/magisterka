import sys
input = sys.stdin.readline


class  UnionFind:
    def  __init__(self, n):
        self.parent = list(range(0, n))
        self.size = [1] * n
    def  find(self, a):
        acopy = a
        while  self.parent[a] != a:
            a = self.parent[a]
        while  acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def  union(self, a, b):
        a, b = self.find(a), self.find(b)
        if  a == b:
            return None
        if  self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def main():
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n):
        a[i], b[i] = map(int, input().split())

    uf = UnionFind(n + 1)
    for i in range(1, n):
        uf.union(a[i], b[i])
        uf.union(a[i], 0)
        uf.union(b[i], 0)

    mod = 10**9 + 7
    result = [0] * (n + 1)
    for k in range(1, n + 1):
        group = uf.find(k)
        result[k] = (uf.size[group] * pow(2, uf.size[group] - 1, mod)) % mod
    for i in range(1, n + 1):
        print(result[i])

if  __name__ == "__main__":
    main()