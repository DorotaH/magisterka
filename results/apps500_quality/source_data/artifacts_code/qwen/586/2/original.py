MOD = 998244353

def count_suitable_colorings(n, k):
    if n == 1:
        return 0
    
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    
    for i in range(1, n):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
    
    total_beautiful = sum(dp[n-1]) % MOD
    
    if k == 1:
        return 0
    
    dp2 = [[0] * 2 for _ in range(n)]
    dp2[0][0] = 1
    dp2[0][1] = 1
    
    for i in range(1, n):
        dp2[i][0] = (dp2[i-1][0] + dp2[i-1][1]) % MOD
        dp2[i][1] = (dp2[i-1][0] + dp2[i-1][1]) % MOD
    
    total_suitable = (total_beautiful - 2) % MOD
    
    return total_suitable

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])

# Print output
print(count_suitable_colorings(n, k))
