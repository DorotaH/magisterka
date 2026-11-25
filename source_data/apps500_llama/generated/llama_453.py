import sys
import math

def solve():
    n, m = map(int, input().split())
    intervals = []
    for _ in range(m):
        l, r = map(int, input().split())
        intervals.append((l-1, r-1))
    
    intervals.sort(key=lambda x: x[1])

    dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = dp[i][j-1]
            if j >= intervals[i][0]:
                dp[i][j] = max(dp[i][j], dp[i-1][j - intervals[i][0] - 1] + (j - intervals[i][0]) * (intervals[i][1] - j + 1))

    ans = []
    i, j = m, n
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append('1')
            j -= intervals[i-1][0] + 1
            i -= 1
        else:
            ans.append('0')
            j -= 1
    print(''.join(reversed(ans)))

if __name__ == '__main__':
    solve()
