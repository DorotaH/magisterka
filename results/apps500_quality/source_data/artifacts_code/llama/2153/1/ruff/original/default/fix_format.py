import sys

n = int(input())
h = list(map(int, input().split()))

if n == 2:
    print(1)
    sys.exit()

dp = [float("inf")] * n
dp[0] = 0

prev_lower = -1
prev_higher = -1
prev_min = h[0]
for i in range(1, n):
    if h[i] <= prev_min:
        dp[i] = dp[i - 1] + 1
        prev_lower = i
    elif h[i] > prev_min:
        if h[i] > prev_higher:
            dp[i] = min(dp[i], dp[prev_lower] + 1)
        if prev_lower != -1 and h[i] < prev_min:
            dp[i] = min(dp[i], dp[prev_lower] + 2)
        if prev_higher != -1 and prev_min < h[i]:
            dp[i] = min(dp[i], dp[prev_higher] + 2)
        prev_higher = i
    prev_min = min(prev_min, h[i])

print(dp[n - 1])
