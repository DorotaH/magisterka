MOD=998244353

def  count_emotional_orders(n, a):
    a.sort()
    dp=[1]*(n + 1)
    for i in range(1, n + 1):
        dp[i]=(2 * dp[i - 1])%MOD
    for i in reversed(range(n)):
        dp[i]=(dp[i]-dp[1 + i]+MOD)%MOD
    for i in range(1, n):
        if  2 * a[i]<=a[i-1]:
            dp[i] = 0
    return dp[0]

import sys
input=sys.stdin.read
data=input().split()
n, a = int(data[0]), list(map(int, data[1:]))
print(count_emotional_orders(n, a))
