n, k = map(int, input().split())
s = input()
t = input()

dp = [0] * (n + 1)
dp[0] = 1

for i in range(0, n):
    dp[1 + i] = 1 + dp[i]
    if s[i] == "a":
        dp[1 + i] = max(dp[1 + i], 1 + dp[i])

    if t[i] == "b":
        dp[1 + i] = max(dp[1 + i], dp[i] + k)

    for j in range(0, i):
        if s[j] == "a" and s[i] == "b":
            dp[1 + i] = max(dp[1 + i], dp[j] + ((i - j) * (k - 1)))

print(dp[n])
