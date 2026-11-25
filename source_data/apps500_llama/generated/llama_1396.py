import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.t = [[0]*(n+1) for _ in range(2)]

    def update(self, i, x, t):
        while i <= self.n:
            self.t[t][i] += x
            i += i & -i

    def query(self, r, t):
        res = 0
        while r:
            res += self.t[t][r]
            r -= r & -r
        return res

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_tree = FenwickTree(n)
    max_prefix = [0]*(n+1)
    for i in range(n):
        max_prefix[i+1] = max(max_prefix[i], a[i])
        max_tree.update(i+1, 1, 0)
        max_tree.update(i+1, 1, 1)

    min_tree = FenwickTree(n)
    min_prefix = [0]*(n+1)
    for i in range(n):
        min_prefix[i+1] = min(min_prefix[i], b[i])
        min_tree.update(i+1, 1, 0)
        min_tree.update(i+1, 1, 1)

    res = 0
    for l in range(1, n+1):
        for r in range(l, n+1):
            res += (max_prefix[r] == min_prefix[l])
            if l > 1:
                res -= max_tree.query(l-1, 0) + max_tree.query(r, 0) - max_tree.query(r, 1)
            if l > 1:
                res -= min_tree.query(l-1, 0) + min_tree.query(r, 0) - min_tree.query(r, 1)

    print(res)

if __name__ == "__main__":
    main()
