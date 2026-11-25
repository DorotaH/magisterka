import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

if not N == 1:
    dp = [0] * (N + 1)
    dp[1] = K
    dp[2] = K * (K - 1)
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] * (K - 1)
    print(dp[N])
else:
    print(K)
