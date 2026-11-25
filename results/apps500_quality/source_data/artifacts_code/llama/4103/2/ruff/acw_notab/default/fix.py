def max_distance(n, b, a, s):
    dp = [[0] * (a + 1) for _ in range(1 + b)]
    
    for i in range(1, 1 + n):
        for j in range(1 + b):
            if i > 1:
                for k in range(a + 1):
                    if s[i - 1] == 1:
                        dp[j][k] = max(dp[j][k], 1 + dp[j][k])
                    if 0 < j and k > 0:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - 1][k - 1])
                    if 0 < j and a > k:
                        dp[j][k] = max(dp[j][k], dp[j - 1][k] + 1)
        for k in range(a + 1):
            dp[j][k] = max(dp[j][k], dp[j][k])
    
    ans = 0
    for j in range(1 + b):
        for k in range(a + 1):
            ans = max(ans, dp[j][k])
    
    return ans


n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(max_distance(n, b, a, s))
