MOD = 998244353

def count_emotional_orders(n, a):
    a.sort()
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 2) % MOD
    for i in range(n - 1, -1, -1):
        dp[i] = (dp[i] - dp[i + 1] + MOD) % MOD
    for i in range(1, n):
        if 2 * a[i] <= a[i - 1]:
            dp[i] = 0
    return dp[0]

import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))
print(count_emotional_orders(n, a))
