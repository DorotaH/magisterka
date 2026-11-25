import sys


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[-1] * (1 + n) for _ in range(4)]

    def update(self, x, v):
        x = x + self.n
        self.tree[0][x] = v
        while x > 1:
            x = x >> 1
            self.tree[0][x] = max(self.tree[0][x * 2], self.tree[0][x * 2 + 1])

    def query(self, l, r):
        l = l + self.n
        r += 1 + self.n
        res = -1
        while l < r:
            if l & 1:
                res = max(res, self.tree[0][l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[0][r])
            l = l >> 1
            r = r >> 1
        return res


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    visitors = []
    for _ in range(m):
        l, r = map(int, input().split())
        visitors.append((l - 1, r))

    tree = SegmentTree(n)
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i, (l, r) in enumerate(visitors):
        for j in reversed(range(r)):
            if dp[j][i] == -1:
                continue
            tree.update(j + 1, i)
            for k in range(1 + j, r):
                if not dp[k][i + 1] == -1:
                    dp[k][i + 1] = max(dp[k][i + 1], i)
                else:
                    dp[k][i + 1] = i
                    tree.update(k + 1, i)

    ans = ["1"] * n
    i = n - 1
    j = n
    while i > 0:
        while j > 0 and dp[i][j] == -1:
            j = j - 1
        if j == 0:
            break
        ans[i] = "0"
        i = i - 1
        j = tree.query(1 + i, 1 + i)

    print("".join(ans))


if __name__ == "__main__":
    main()
