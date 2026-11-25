MOD = 998244353


def count_good_arrays(n, k, a):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if a[i] == -1:
            for j in range(n, i, -1):
                dp[j] = (dp[j] + dp[j - 2]) % MOD
        else:
            for j in range(n, i, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
    return dp[n]


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))

# Calculate and print the result
print(count_good_arrays(n, k, a))
