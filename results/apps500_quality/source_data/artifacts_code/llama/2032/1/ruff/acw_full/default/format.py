from collections import deque


def main():
    n, m, k = map(int, input().split())
    a, b, c = [], [], []
    for _ in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)

    portals = []
    for _ in range(m):
        u, v = map(int, input().split())
        portals.append((u - 1, v - 1))

    dp = [[[float("-inf")] * (1 + n) for _ in range(1 + n)] for _ in range(1 + n)]
    dp[0][0][0] = 0
    for i in range(1, 1 + n):
        for j in range(i + 1):
            for l in range(k + 1):
                if l >= a[i - 1]:
                    dp[i][j][l] = max(
                        dp[i - 1][j][l], dp[i - 1][j][l - a[i - 1]] + c[i - 1]
                    )
                    if 0 < j:
                        dp[i][j][l] = max(dp[i][j][l], c[i - 1] + dp[i - 1][j - 1][l])
                    for u, v in portals:
                        if u == i - 1:
                            dp[i][j][l] = max(dp[i][j][l], dp[v][j][l])
                    for u, v in portals:
                        if u == i - 1:
                            dp[v][j][l] = max(dp[v][j][l], dp[i][j][l])

    ans = 0
    for i in range(1 + n):
        for l in range(k + 1):
            if l >= a[n - 1]:
                ans = max(ans, dp[n][i][l])

    if ans == float("-inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
