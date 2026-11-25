MOD = 998244353

def count_good_arrays(n, k, a):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0]=1
    for i in range(n):
        for j in range(k + 1):
            if a[i] == -1:
                for x in range(1, k + 1):
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * x) % MOD
            else:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
                if j > 0:
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j - 1]) % MOD
    return  dp[n][0]

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(count_good_arrays(n, k, a))