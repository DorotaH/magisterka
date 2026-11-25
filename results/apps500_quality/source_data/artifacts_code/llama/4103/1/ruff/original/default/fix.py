
def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[-1 for _ in range(a + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(a + 1):
            if i > 1:
                if s[i - 1] == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][min(j + 1, a)] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][max(0, j - 1)], dp[i - 1][min(j, a)] + 1)
            else:
                if s[i - 1] == 1:
                    dp[i][j] = max(0, dp[i - 1][j] + 1)
                else:
                    dp[i][j] = max(0, dp[i - 1][max(0, j - 1)])

    ans = 0
    for i in range(a + 1):
        ans = max(ans, dp[n][i])

    print(ans)

if __name__ == "__main__":
    main()
