import sys


def solve():
    n, b, a = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(1, n + 1):
        dp[i][0] = -1
        dp[i][1] = -1

        if s[i - 1] == 1:
            if b > 0:
                dp[i][0] = dp[i - 1][0] + 1
            if i > 1 and a > 0:
                dp[i][1] = dp[i - 1][1] + 1
        else:
            if b > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + 1)
            if a > 0 and i > 1:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)

        if b > 0 and a > 0 and s[i - 1] == 1:
            if dp[i - 1][0] > dp[i - 1][1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + 1 + min(b, a))
            else:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1 + min(b, a))

    ans = max(dp[n][0], dp[n][1])
    print(ans)

if __name__ == "__main__":
    solve()
