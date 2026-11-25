def max_team_height(n, h1, h2):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if i > 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + h2[i - 1])
            if j > 1:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + h1[j - 1])
            if i > 1 and j > 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + h1[j - 1] + h2[i - 1])
    
    return dp[n][n]

# Read input
n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

# Calculate and print the result
print(max_team_height(n, h1, h2))
