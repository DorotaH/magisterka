#!/usr/bin/env python3


M = 7 + 10**9


def solve(n, m, s, lst):

    cnt, t = [0] * n, 0
    for i in range(n):
        if s[i] == "1":
            t = t + 1
        cnt[i] = t

    dp = []
    for _ in range(n + 1):
        dp.append([0] * (n + 1))
    dp[0][0] = 1
    r = 0
    j = 0
    for i in range(n):
        while m > j:
            lj, rj = lst[j]
            if not lj <= i:
                break
            else:
                r = max(r, rj)
                j += 1
        if r <= i:
            c = cnt[i]
            if c > 0:
                dp[i + 1][cnt[i]] = (dp[i][c] + dp[i][c - 1]) % M
            else:
                dp[i + 1][0] = dp[i][0]
        else:
            for k in range(max(0, cnt[r] - r + i), min(i + 1, cnt[r]) + 1):
                if k > 0:
                    dp[i + 1][k] = (dp[i][k] + dp[i][k - 1]) % M
                else:
                    dp[i + 1][0] = dp[i][0]

    return dp[n][cnt[n - 1]]


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    s, lst = input(), []
    for _ in range(m):
        l, r = input().split()
        l = int(l) - 1
        r = int(r) - 1
        lst.append((l, r))

    print(solve(n, m, s, lst))


def __starting_point():
    main()


__starting_point()
