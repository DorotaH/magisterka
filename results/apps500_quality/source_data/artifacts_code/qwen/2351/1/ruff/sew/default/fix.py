MOD = 998_244_353


def  count_ways(n, k, len, arr):
    dp=[0]*(n + 1)
    dp[0]=1
    for  i in  range(n):
        if not arr[i] == -1:
            dp[i + 1] = dp[i]
        else:
            dp[i + 1] = 0
            for j in range(1, k + 1):
                if i - len >= 0 and arr[i - len] == j:
                    dp[i + 1] += dp[i]
                else:
                    dp[i + 1] += dp[i] * k
                dp[i + 1] %= MOD
    return  dp[n]

# Read input
n, k, len = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(count_ways(n, k, len, arr))
