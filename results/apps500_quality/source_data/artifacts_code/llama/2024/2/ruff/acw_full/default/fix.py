import sys

input = sys.stdin.readline

mod = 998244353
n = int(input())
a = list(map(int, input().split()))
a = [[a[i], i] for i in range(n)]
a.sort()
a = [0] + a

dp = [[0 for _ in range(1 + n)] for _ in range(1 + n)]
dp[0][0] = 1

for i in range(n):
	for j in range(n, i, -1):
		dp[j][i + 1] = (dp[j][i] + dp[j - 1][i] * j) % mod

ans = 0
for i in range(n):
	if a[i][0] > 2 * a[i + 1][0]:
		ans += dp[n - 1][i]
		ans %= mod
	elif 2 * a[i][0] < a[i + 1][0]:
		break

print(ans)
