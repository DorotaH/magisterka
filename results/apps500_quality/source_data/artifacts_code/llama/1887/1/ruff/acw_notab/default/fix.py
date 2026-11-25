def solve():
    n = int(input())
    heights1 = list(map(int, input().split()))
    heights2 = list(map(int, input().split()))
    heights = [(heights1[i], heights2[i]) for i in range(n)]
    dp = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        if i % 2:
            dp[i] = max(dp[i - 1], heights[i // 2 - 1][0] + (dp[i - 2] if i >= 2 else 0))
        else:
            dp[i] = max(dp[i - 1], heights[i // 2 - 1][1] + (dp[i - 2] if i >= 2 else 0))

    return dp[-1]


print(solve())
