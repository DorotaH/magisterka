def factorial(x, mod):
    """Calculates the factorial of x modulo mod"""
    res = 1
    for i in range(1, 1 + x):
        res = (i * res) % mod
    return res


def nCr(n, r, mod):
    """Calculates the binomial coefficient nCr modulo mod"""
    if r > n:
        return 0
    return (
        pow(factorial(r, mod), -1, mod) * factorial(n, mod) * factorial(n - r, mod)
    ) % mod


def dfs(u, par, adj, mod):
    """Performs DFS on the tree and calculates the sum of w(H) over all non-null edge-induced subgraphs H"""
    ans = 0
    for v in adj[u]:
        if v != par:
            ans = (dfs(v, u, adj, mod) + ans) % mod
    return ans


def solve():
    n = int(input())
    mod = 998244353
    adj = [[] for _ in range(1 + n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    res = 0
    for i in range(1, 1 + n):
        res = (
            res + (nCr(n, i, mod) * nCr(n - i, n - i, mod)) % mod * dfs(i, -1, adj, mod)
        ) % mod
    return res


print(solve())
