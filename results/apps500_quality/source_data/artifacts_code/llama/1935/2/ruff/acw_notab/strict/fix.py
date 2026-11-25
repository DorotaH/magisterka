import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    safety_islands = sorted(list(map(int, sys.stdin.readline().split())))
    g, r = map(int, sys.stdin.readline().split())

    if safety_islands[0] != 0 or safety_islands[-1] != n:
        print(-1)
        return

    dp = [[float('inf')] * (1 + m) for _ in range(1 + m)]
    dp[0][0] = 0

    for i in range(m):
        for j in range(i + 1):
            if j > 0:
                dp[i + 1][j] = min(dp[i + 1][j], g + dp[i][j])
            if m > j:
                dp[i + 1][1 + j] = min(dp[i + 1][1 + j], g + dp[i][j])

            if j > 0:
                if safety_islands[i + 1] - safety_islands[i] == 1:
                    dp[i + 1][j] = min(dp[i + 1][j], r + dp[i][j - 1] + g)
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], r + dp[i][j - 1])

            if m > j:
                if safety_islands[i + 1] - safety_islands[i] == -1:
                    dp[i + 1][1 + j] = min(dp[i + 1][1 + j], r + dp[i][j - 1] + g)
                else:
                    dp[i + 1][1 + j] = min(dp[i + 1][1 + j], r + dp[i][j - 1])

    ans = float('inf')
    for j in range(m):
        ans = min(ans, g + dp[m][j] + (g + r) * ((n - safety_islands[-1]) // (g + r)))

    print(ans if ans != float('inf') else -1)


if __name__ == "__main__":
    main()
