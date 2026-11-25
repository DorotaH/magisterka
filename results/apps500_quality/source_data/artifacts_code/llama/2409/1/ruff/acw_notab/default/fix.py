

def can_koa_reach_island(n, k, l, d):
    p = [0] * (2 * k)
    for i in range(k):
        p[i] = -1
        p[2 * k - i - 1] = 1
    for i in range(k):
        p[i] = max(-l, min(p[i], l - d[i]))

    dp = [float('inf')] * (1 + n)
    dp[0] = 0
    for i in range(1, 1 + n):
        for j in range(k):
            if d[i - 1] + p[j] <= l:
                dp[i] = min(dp[i], 1 + dp[i - 1])
            if i >= k and d[i - 1] + p[j] <= l:
                dp[i] = min(dp[i], 1 + dp[i - k])

    return dp[n] != float('inf')


t = int(input())
for _ in range(t):
    n, k, l = map(int, input().split())
    d = list(map(int, input().split()))
    if can_koa_reach_island(n, k, l, d):
        print("Yes")
    else:
        print("No")
