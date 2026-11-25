MOD = 998_244_353

def count_ways(n, k, len, arr):
    if len == 1:
        return (k**arr.count(-1))%MOD

    dp = []
    for _ in range(n+1):
        dp.append([0] * (k+1))
    dp[0][0]=1

    for i in range(0, n):
        if arr[i] == -1:
            for j in range(1, k+1):
                dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % MOD
        else:
            dp[i+1][arr[i]] = dp[i][arr[i]]

    return dp[n][0]

# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
len = int(data[2])
arr = list(map(int, data[3:]))

# Output the result
print(count_ways(n, k, len, arr))
