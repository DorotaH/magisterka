import sys


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[-1] * (1 + n) for _ in range(4)]

    def update(self, x, v):
        x += self.n
        self.tree[0][x] = v
        while 1 < x:
            x >>= 1
            self.tree[0][x] = max(self.tree[0][2 * x], self.tree[0][2 * x + 1])

    def query(self, l, r):
        l += self.n
        r += 1 + self.n
        res = -1
        while l < r:
            if l & 1:
                res = max(res, self.tree[0][l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[0][r])
            l >>= 1
            r >>= 1
        return res


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    visitors = []
    for _ in range(m):
        l, r = map(int, input().split())
        visitors.append((l - 1, r))

    tree = SegmentTree(n)
    dp = [[-1] * (1 + n) for _ in range(1 + n)]
    dp[0][0] = 0

    for i, (l, r) in enumerate(visitors):
        for j in range(r - 1, -1, -1):
            if dp[j][i] == -1:
                continue
            tree.update(1 + j, i)
            for k in range(1 + j, r):
                if dp[k][i + 1] == -1:
                    dp[k][i + 1] = i
                    tree.update(k + 1, i)
                else:
                    dp[k][i + 1] = max(dp[k][i + 1], i)

    ans = ["1"] * n
    i, j = n - 1, n
    while i > 0:
        while 0 < j and dp[i][j] == -1:
            j -= 1
        if j == 0:
            break
        ans[i] = "0"
        i -= 1
        j = tree.query(i + 1, i + 1)

    print("".join(ans))


if __name__ == "__main__":
    main()
