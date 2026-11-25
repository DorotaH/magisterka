import sys

input = sys.stdin.readline


class LCA:
    def __init__(self, n, tree):
        self.n = n
        self.tree = tree
        self.log = [0] * (n + 1)
        self.log[1] = 0
        for i in range(2, 1 + n):
            self.log[i] = self.log[i >> 1] + 1

        self.parent = [[0] * (self.log[n] + 1) for _ in range(0, n)]
        self.depth = [0] * n

        for i in range(n):
            self.depth[i] = 1
        self.parent[0][0] = -1

        for i in range(1, n):
            self.parent[i][0] = tree[i][0]

        for j in range(1, 1 + self.log[n]):
            for i in range(0, n):
                if self.parent[i][j - 1] != -1:
                    self.parent[i][j] = self.parent[self.parent[i][j - 1]][j - 1]

        self.seg_tree = [[0] * (n + 1) for _ in range(0, 4)]

    def update(self, index, value):
        index += self.n
        self.seg_tree[0][index] = value
        for i in range(1, 4):
            self.update_segment_tree(
                index >> i, self.seg_tree[i - 1][index ^ (1 << (i - 1)), index]
            )

    def update_segment_tree(self, index, left, right):
        self.seg_tree[0][index] = self.query(left, right)

    def query(self, left, right):
        left += self.n
        right += self.n
        answer = 0
        for i in range(3, -1, -1):
            if left & (1 << i):
                left = left ^ (1 << i)
                answer = answer | self.seg_tree[i][left, self.n]
                left = left + 1
            if right & (1 << i):
                answer = answer | self.seg_tree[i][self.n, right ^ (1 << i)]
                right = right - 1
        return answer

    def lca(self, a, b):
        if self.depth[b] > self.depth[a]:
            a, b = b, a
        for j in range(1 + self.log[self.depth[a]], -1, -1):
            if (self.depth[a] - (1 << j)) >= self.depth[b]:
                a = self.parent[a][j]
        if b == a:
            return a
        for j in range(self.log[self.depth[a]] + 1):
            if self.parent[b][j] != self.parent[a][j]:
                a = self.parent[a][j]
                b = self.parent[b][j]
        return self.parent[a][0]

    def distance(self, a, b):
        return self.depth[a] + self.depth[b] - (2 * self.depth[self.lca(a, b)])

    def is_ancestor(self, a, b):
        return self.depth[b] <= self.depth[a] and self.lca(a, b) == a


def solve():
    n, m = map(int, input().split())
    tree = []
    for _ in range(n):
        tree.append([])
    for i in range(0, n - 1):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    lca = LCA(n, tree)

    for i in range(0, n):
        lca.update(i, 1)

    for i in range(0, m):
        k = int(input())
        v = list(map(int, input().split()))
        v = [x - 1 for x in v]

        found = False
        for u in v:
            if lca.is_ancestor(1, u):
                found = True
                break
        if not found:
            print("NO")
            continue

        ancestors = [1]
        for u in v:
            ancestors.append(lca.lca(1, u))
        ancestors = list(set(ancestors))

        for u in v:
            lca.update(u, lca.distance(1, u) - 1)

        for u in v:
            lca.update(u, 0)

        for u in ancestors:
            lca.update(u, 1)

        answer = lca.query(0, n - 1)
        if answer == len(ancestors):
            print("YES")
        else:
            print("NO")


solve()
