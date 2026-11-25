def max_beauty_pictures(n, k, x, a):
    if n < k * x:
        return -1
    
    dp = [[-1] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if i >= k:
                dp[i][j] = max(dp[i][j], dp[i - k][j - 1] + sum(a[i - k:i]))
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    
    return dp[n][x]

# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
x = int(data[2])
a = list(map(int, data[3:]))

# Output result
print(max_beauty_pictures(n, k, x, a))
