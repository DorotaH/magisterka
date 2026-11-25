import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split()))


def read_string():
    return input().strip()


def read_strings():
    return input().strip().split()


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.color_groups = {i: set() for i in range(3)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
            self.color_groups[root_y] |= self.color_groups[root_x]
            self.color_groups[root_x].clear()
            return True
        return False

    def add_point(self, color, x):
        self.color_groups[self.find(x)].add(color)


n = read_int()
uf = UnionFind(n + 1)
points = []
for i in range(n):
    p, c = read_string()
    points.append((int(p), c))

points = sorted(points, key=lambda x: x[0])
cost = 0
for i in range(1, n):
    p1, c1 = points[i - 1]
    p2, c2 = points[i]
    cost += abs(p2 - p1)
    if c1 != c2:
        uf.union(i, i + 1)

cost += (
    uf.color_groups[uf.find(0)].issubset({2})
    * (uf.color_groups[1].issubset({0}) + uf.color_groups[2].issubset({0}))
    * (uf.color_groups[0].issubset({1}) + uf.color_groups[2].issubset({1}))
    * (uf.color_groups[0].issubset({1}) + uf.color_groups[1].issubset({2}))
    * 2
)
print(cost)
