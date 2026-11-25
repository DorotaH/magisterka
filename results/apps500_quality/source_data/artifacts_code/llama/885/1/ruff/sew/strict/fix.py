import sys

input, mod = sys.stdin.readline, 998244353

def read_int():
    return  int(input())

def read_ints():
    return  map(int, input().split())

def read_str():
    return  input().strip()

def solve():
    n=read_int()
    adj=[list() for  _ in  range(0, n)]
    for  _ in  range(0, n-1):
        u, v = read_ints()
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    dp = [0] * n
    ans = 0
    for  i in  range(0, n):
        if  dp[i] == 0:
            dfs(i, adj, dp)

    ans=1
    for  i in  range(0, n):
        ans = (ans * 2**dp[i] % mod) % mod
    print(ans)

def dfs(v, adj, dp):
    stack = [v]
    parent = [-1] * len(adj)
    parent[v]=v
    while  stack:
        v=stack.pop()
        for  u in  adj[v]:
            if parent[u]==-1:
                parent[u] = v
                stack.append(u)
                if  dp[u] == 0:
                    dfs(u, adj, dp)
                dp[v] += dp[u]
    return

solve()
