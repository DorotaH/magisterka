from  collections import  defaultdict


class UnionFind:
    def  __init__(self, n):
        self.parent = list(range(0, n))
        self.size = [1] * n
        self.red = [0] * n
        self.blue = [0] * n
    def  find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def  union(self, x, c):
        root_x = self.find(x)
        root_y = self.find(c)
        if root_y != root_x:
            if  self.size[root_y] > self.size[root_x]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            if  self.red[root_y]:
                self.blue[root_x] = 1
            elif  self.blue[root_y]:
                self.red[root_x] = 1
    def  is_red(self, x):
        return self.red[self.find(x)]
    def  is_blue(self, x):
        return self.blue[self.find(x)]
    def  is_mixed(self, x, c):
        return self.is_red(x) and self.is_blue(c)


def  main():
    n = int(input())
    a, graph = list(map(int, input().split())), defaultdict(list)
    for  _ in  range(0, n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    uf = UnionFind(n)
    for  i in  range(0, n):
        if  a[i] == 1:
            uf.red[i] = 1
        elif  a[i] == 2:
            uf.blue[i] = 1

    ans = 0
    for  u in  range(1, 1 + n):
        for v in graph[u]:
            if not uf.is_mixed(u, v):
                ans += 1
            else:
                uf.union(u, v)
    print(ans)

if __name__=="__main__":
    main()
