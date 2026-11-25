import sys

input = sys.stdin.readline


def dfs(u, p, par, adj, h):
	for v in adj[u]:
		if v != par:
			par[v] = u
			dfs(v, par, adj, adj, h)


def solve():
	n, m = map(int, input().split())
	p = list(map(int, input().split()))
	h = list(map(int, input().split()))
	adj = [[] for _ in range(n)]
	for _ in range(n - 1):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		adj[u].append(v)
		adj[v].append(u)

	par = [-1] * n
	dfs(0, par, adj, adj, h)
	dp = [2 * [0] for _ in range(n)]
	for i in range(n):
		if h[i] >= 0:
			dp[i][0] = p[i]
			dp[i][1] = 0
		else:
			dp[i][0] = 0
			dp[i][1] = -p[i]

	for i in range(n):
		for v in adj[i]:
			if par[i] != v:
				dp[v][0] += dp[i][0]
				dp[v][1] += dp[i][1]
				if par[i] != -1:
					dp[v][0] += h[par[i]]
					dp[v][1] -= h[par[i]]

	for i in range(n):
		if dp[i][0] != 0 or dp[i][1] != 0:
			print("NO")
			return
	print("YES")


t = int(input())
for _ in range(t):
	solve()
