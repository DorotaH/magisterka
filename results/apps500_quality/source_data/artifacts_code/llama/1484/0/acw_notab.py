from sys import stdin
input = stdin.readline

mod = 998244353

n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == 2:
    if a[0] == -1 and a[1] == -1:
        print((k + 1) * (k + 1))
    else:
        print(0)
    exit()

dp = [[0 for _ in range(1 + n)] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    dp[i][0] = (k + 1) * dp[i - 1][0]
    dp[i][1] = (k + 1) * dp[i - 1][1]
    for j in range(2, min(i, n - i)):
        dp[i][j] = (k + 1) * (k + 1) * dp[i - 1 - j][j - 1]
        if a[i] != -1 and a[i] == a[i - j]:
            dp[i][j] = (dp[i][j] - dp[i - 1][j]) % mod
        if a[i - j] != -1 and a[i - j] == a[i]:
            dp[i][j] = (dp[i][j] - dp[i - 1][j - 1]) % mod

ans = 0
for i in range(0, n, 2):
    ans = (ans + dp[i][n - 1 - i]) % mod

print(ans)
