import math


def solve():
    n, m = map(int, input().split())
    intervals = []
    for _ in range(m):
        l, r = map(int, input().split())
        intervals.append((l - 1, r - 1))

    intervals.sort(key=lambda x: x[1])

    dp = [[-math.inf] * (1 + n) for _ in range(1 + m)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(1 + n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j]) if i > 0 else dp[i][j - 1]
            if intervals[i][0] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - intervals[i][0] - 1] + (j - intervals[i][0]) * (intervals[i][1] - j + 1))

    ans = []
    i, j = m, n
    while i > 0:
        if dp[i][j] != dp[i - 1][j]:
            ans.append('1')
            j -= intervals[i - 1][0] + 1
            i -= 1
        else:
            ans.append('0')
            j -= 1
    print(''.join(reversed(ans)))


if __name__ == '__main__':
    solve()
