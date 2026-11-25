def solve(n, m, a):
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, 1 + n):
        for j in range(m, a[i - 1] - 1, -1):
            dp[j] |= dp[j - a[i - 1]]
    return "YES" if dp[m] else "NO"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, a))
