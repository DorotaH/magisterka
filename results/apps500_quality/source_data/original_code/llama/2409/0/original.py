import sys

def can_reach_island(n, k, l, d):
    p = [0] * (2 * k)
    for i in range(k):
        p[i] = i
    for i in range(k, 2 * k):
        p[i] = -1 - (i - k)

    max_depths = [d[i] + p[i % (2 * k)] for i in range(n)]

    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        for j in range(i + 1):
            if max_depths[i] <= l and dp[i - j]:
                dp[i + 1] = True
                break

    return dp[n]

t = int(sys.stdin.readline())
for _ in range(t):
    n, k, l = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    print('Yes' if can_reach_island(n, k, l, d) else 'No')
