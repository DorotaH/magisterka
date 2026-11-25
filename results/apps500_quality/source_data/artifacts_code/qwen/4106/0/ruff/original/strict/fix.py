def max_beauty_sum(n, k, x, a):
    if k > x:
        return -1

    dp = [[0] * (x + 1) for _ in range(n + 1)]
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if i < k:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + prefix_sum[i] - prefix_sum[i - k])

    return dp[n][x]

# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
x = int(data[2])
a = list(map(int, data[3:]))

# Output result
print(max_beauty_sum(n, k, x, a))
