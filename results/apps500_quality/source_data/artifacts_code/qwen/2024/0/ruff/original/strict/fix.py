MOD = 998244353

def count_emotional_orders(n, a):
    a.sort()
    dp = [0] * (n + 1)
    dp[0] = 1
    for x in a:
        new_dp = [0] * (n + 1)
        for j in range(n + 1):
            if 2 * x <= j:
                new_dp[j] += dp[j - 2 * x]
                new_dp[j] %= MOD
            if x >= 2 * j:
                new_dp[j] += dp[j]
                new_dp[j] %= MOD
        dp = new_dp
    return dp[0]

import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))
print(count_emotional_orders(n, a))
