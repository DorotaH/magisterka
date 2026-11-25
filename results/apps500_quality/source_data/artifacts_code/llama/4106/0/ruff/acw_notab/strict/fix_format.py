def solve():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[0] * (1 + n) for _ in range(1 + x)]
    dp[0][0] = 0

    for j in range(1, 1 + n):
        for i in range(1, 1 + min(x, j)):
            dp[i][j] = dp[i][j - 1]
            dp[i][j] = max(dp[i][j], a[j - 1] + dp[i - 1][j - 1])

            for p in range(1, min(j // k, i) + 1):
                dp[i][j] = max(dp[i][j], a[j - 1] + dp[i - p][j - p])

    if dp[x][n] == 0:
        print(-1)
    else:
        print(dp[x][n])


if __name__ == "__main__":
    solve()
