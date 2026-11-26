from collections import defaultdict
import sys
import random

sys.setrecursionlimit(pow(10, 6))

MOD = 7 + 10**9


def dfs(node, parent):
    dp[node][0] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            dp[node][1] += dp[neighbor][0]
            dp[node][1] %= MOD
            dp[node][0] += dp[neighbor][1]
            dp[node][0] %= MOD


def solve():
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    dp = [[0, 0] for _ in range(N + 1)]

    for k in range(1, 1 + N):
        dfs(k, -1)
        for i in range(1, 1 + N):
            if i != k:
                dp[k][0] += dp[i][1]
                dp[k][0] %= MOD
                dp[k][1] += dp[i][0]
                dp[k][1] %= MOD
        dp[k][0] += 1
        dp[k][0] %= MOD
        dp[k][1] += 1
        dp[k][1] %= MOD
        for i in range(1, 1 + N):
            if i != k:
                dp[i][0] = dp[k][1]
                dp[i][1] = dp[k][0]

    for k in range(1, 1 + N):
        print(dp[k][0])


if __name__ == "__main__":
    solve()
