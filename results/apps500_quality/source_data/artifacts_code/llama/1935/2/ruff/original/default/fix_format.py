import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    safety_islands = sorted(list(map(int, sys.stdin.readline().split())))
    g, r = map(int, sys.stdin.readline().split())

    if safety_islands[0] != 0 or safety_islands[-1] != n:
        print(-1)
        return

    dp = [[float("inf")] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(m):
        for j in range(i + 1):
            if j > 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + g)
            if j < m:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + g)

            if j > 0:
                if safety_islands[i + 1] - safety_islands[i] == 1:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1] + r + g)
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1] + r)

            if j < m:
                if safety_islands[i + 1] - safety_islands[i] == -1:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j - 1] + r + g)
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j - 1] + r)

    ans = float("inf")
    for j in range(m):
        ans = min(ans, dp[m][j] + g + (r + g) * ((n - safety_islands[-1]) // (g + r)))

    print(ans if ans != float("inf") else -1)


if __name__ == "__main__":
    main()
