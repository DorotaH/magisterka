
s = input()

n = len(s)
mod = 2019
ans = 0
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = 10 * dp[i - 1]
    for j in range(2, 10):
        if dp[i - j] % mod == 0:
            dp[i] += dp[i - j]

    dp[i] %= mod

    for k in range(1, i):
        dp[i] -= dp[k]
        if dp[i] < 0:
            dp[i] += mod
for i in range(n):
    for j in range(i, n):
        if (int(s[i:j + 1]) % mod == 0):
            ans += 1
print(ans)
