def  max_distance(n, b, a, s):
    dp = []
    for _ in range(b + 1):
        dp.append([0] * (a + 1))
    
    for i in range(1, 1 + n):
        for  j in  range(b + 1):
            if  i>1:
                for  k in  range(a + 1):
                    if 1 == s[i - 1]:
                        dp[j][k] = max(dp[j][k], 1 + dp[j][k])
                    if j > 0 and k > 0:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - 1][k - 1])
                    if j > 0 and a > k:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - 1][k])
        for  k in  range(a + 1):
            dp[j][k] = max(dp[j][k], dp[j][k])
    
    ans = 0
    for j in range(b + 1):
        for  k in  range(a + 1):
            ans = max(ans, dp[j][k])
    
    return ans


n, b, a=map(int, input().split())
s=list(map(int, input().split()))
print(max_distance(n, b, a, s))
