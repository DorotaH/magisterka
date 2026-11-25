import sys
input = sys.stdin.readline

mod = 998244353
n = int(input())
a = list(map(int, input().split()))
a = [[a[i], i] for  i in  range(0, n)]
a.sort()
a = [0] + a

dp = []
for _ in range(n + 1):
    dp.append([0 for _ in range(n + 1)])
dp[0][0] = 1

for  i in  range(0, n):
    for j in range(n, i, -1):
        dp[j][i+1] = (dp[j][i] + j * dp[j - 1][i]) % mod

ans = 0
for  i in  range(0, n):
    if a[i][0] > 2 * a[i + 1][0]:
        ans += dp[n - 1][i]
        ans %= mod
    elif 2 * a[i][0]<a[1 + i][0]:
        break

print(ans)
