def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = [a[i - 1] for i in b]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, 1 + n):
            if j == 1:
                dp[i][j] = max(0, a[i - 1])
            else:
                max_score = 0
                for k in range(i):
                    max_score = max(max_score, dp[k][j - 1] + a[i - 1])
                    if a[i - 1] > a[k]:
                        max_score = max(max_score, dp[k][j - 1] + a[k])
                dp[i][j] = max(max_score, dp[i - 1][j])

    score = 0
    for i in range(n):
        if i + 1 in b:
            score += dp[i][i + 1]
        else:
            score += a[i]

    print(score)


if __name__ == "__main__":
    solve()
