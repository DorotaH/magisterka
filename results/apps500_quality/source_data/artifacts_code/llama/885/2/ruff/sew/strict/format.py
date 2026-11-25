def factorial(x, mod):
    """Calculates the factorial of x modulo mod"""
    res = 1
    for i in range(1, x + 1):
        res = (res * i) % mod
    return res


def nCr(n, r, mod):
    """Calculates the binomial coefficient nCr modulo mod"""
    if r > n:
        return 0
    return (
        factorial(n, mod) * pow(factorial(r, mod), -1, mod) * factorial(n - r, mod)
    ) % mod


def dfs(u, par, adj, mod):
    """Performs DFS on the tree and calculates the sum of w(H) over all non-null edge-induced subgraphs H"""
    ans = 0
    for v in adj[u]:
        if v != par:
            ans = (ans + dfs(v, u, adj, mod)) % mod
    return ans


def solve():
    n = int(input())
    mod, adj = 998244353, [[] for _ in range(n + 1)]
    for _ in range(0, n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    res = 0
    for i in range(1, n + 1):
        res = (
            res + (nCr(n, i, mod) * nCr(n - i, n - i, mod)) % mod * dfs(i, -1, adj, mod)
        ) % mod
    return res


print(solve())
