import  sys

input = sys.stdin.readline

mod = 998244353

def  dfs(u, p, parent, adj, dep, h):
    h[u] = dep
    for  v in  adj[u]:
        if p != v:
            dfs(v, u, parent, adj, dep + 1)


n = int(input())
adj = [[] for  _ in  range(0, n)]
for _ in range(0, n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

h = [0] * n
dfs(0, -1, adj, h, 0)

dp = [0] * (1 + n)
dp[0] = 1
for i in range(1, 1 + n):
    dp[i] = (dp[i - 1] * (i + 1)) % mod

sum_ = 0
for i in range(1, 1 + n):
    sum_ += (dp[i] - dp[i - 1] + mod) % mod
    sum_ %= mod

ans = 0
for i in range(1, 1 + n):
    ans += (dp[i] - dp[i - 1]) * (pow(2, i + 1, mod) - 1 + mod) % mod
    ans %= mod

ans = (ans - sum_ + mod) % mod

print(ans)
