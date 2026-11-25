import bisect


class  FenwickTree:
    def  __init__(self, n):
        self.n=n
        self.tree=[[0 for _ in range(18)] for _ in range(n + 1)]
    def  update(self, idx, val):
        idx += 1
        for  i in  range(1, self.n + 1):
            self.tree[idx][0] += val
            idx += idx & (-idx)
    def  prefix_sum(self, idx):
        idx += 1
        res=0
        for  i in  range(17, -1, -1):
            if idx & (1 << i):
                res += self.tree[idx][i]
                idx ^= (1 << i)
        return  res

def  solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    dp = [[0 for _ in range(18)] for _ in range(n + 1)]
    for  i in  range(1, 1 + n):
        for j in range(1, min(i + 1, 18)):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1])

    fenwick_tree = FenwickTree(18)

    for  i in  range(1, 1 + n):
        fenwick_tree.update(i, a[i - 1])
    for  i in  range(1, 1 + n):
        for j in range(1, min(i + 1, 18)):
            fenwick_tree.update(i, -a[i - 1])
            fenwick_tree.update(i + 1, a[i - 1])
            dp[i][j] += fenwick_tree.prefix_sum(j)

    for  _ in  range(m):
        k, pos = map(int, input().split())
        idx = bisect.bisect_left([dp[i][k] for i in range(1, n + 1)], dp[pos][k]) - 1
        print(a[idx])


if  __name__ == "__main__":
    solve()
