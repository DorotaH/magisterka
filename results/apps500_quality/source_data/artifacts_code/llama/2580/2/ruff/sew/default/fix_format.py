import sys
from collections import defaultdict

input = sys.stdin.readline

mod = 10**9 + 7


def dfs(u, par, graph, dp, n):
    dp[u][0] = 1
    for v in graph[u]:
        if par != v:
            dfs(v, u, graph, dp, n)
            dp[u][0] = (dp[v][0] * dp[u][0]) % mod
            for i in range(1, 1 + n):
                dp[u][i] = (dp[u][i - 1] + ((dp[v][i] * (i + 1)) % mod)) % mod


def main():
    t = int(input())
    for _ in range(t):
        n, graph = int(input()), defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        m, primes = int(input()), list(map(int, input().split()))

        dp, tot = [[0] * (n + 1) for _ in range(n + 1)], 1
        for p in primes:
            tot = (tot * p) % mod

        power = [0] * (max(primes) + 1)
        for p in primes:
            power[p] = 1 + power[p - 1]

        dfs(1, -1, graph, dp, n)

        ans = 0
        for i in range(1, 1 + n):
            ans = (ans + dp[1][i] * (i * tot) % mod) % mod

        print(ans)


main()
