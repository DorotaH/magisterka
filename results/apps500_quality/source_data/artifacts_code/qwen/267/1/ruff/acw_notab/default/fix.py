MOD = 998244353


def atMostKDistinctDigits(n, k):
    dp = [[0] * 11 for _ in range(19)]
    dp[0][0] = 1
    for i in range(1, 18):
        for j in range(10):
            for x in range(k):
                dp[i][x] = (dp[i - 1][x] + dp[i][x]) % MOD
                dp[i][1 + x] = (dp[i][1 + x] + dp[i - 1][x]) % MOD
    dp[0][0] = 0
    for i in range(10):
        dp[0][1] = (dp[0][1] + dp[0][0]) % MOD
    
    def getSum(num):
        digits = [int(d) for d in str(num)]
        n = len(digits)
        ans = 0
        for i in range(n):
            ans += dp[n - 1 - i][len(set(digits[:i + 1]))]
            ans %= MOD
        return ans
    
    return (getSum(r) - getSum(l - 1) + MOD) % MOD


import sys

input = sys.stdin.read
data = input().split()
l = int(data[0])
r = int(data[1])
k = int(data[2])
print(atMostKDistinctDigits(r, k) - atMostKDistinctDigits(l - 1, k) + MOD) % MOD
