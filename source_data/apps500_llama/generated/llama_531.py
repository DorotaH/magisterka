a, b = map(int, input().split())
dp = [[0] * (max(a, b) + 2) for _ in range(2)]
dp[0][0] = 0
dp[0][1] = a
dp[0][a + 1] = a * (a + 1) // 2
dp[1][0] = 0
dp[1][1] = b
dp[1][b + 1] = b * (b + 1) // 2

for i in range(2, a + 2):
    for j in range(a + 2, 0, -1):
        if i <= a:
            dp[0][j] = max(dp[0][j], dp[0][j - 1] + i)
        if j <= a:
            dp[0][j] = max(dp[0][j], dp[0][j + 1] + i * (i + 1) // 2)
        if i <= b:
            dp[1][j] = max(dp[1][j], dp[1][j - 1] + i)
        if j <= b:
            dp[1][j] = max(dp[1][j], dp[1][j + 1] + i * (i + 1) // 2)

print(max(dp[0][1], dp[0][2], dp[1][1], dp[1][2]))
