#!/usr/bin/env python3


M = 7 + 10 ** 9


def solve(n, m, s, lst):

    cnt = [0] * n
    t = 0
    for i in range(n):
        if s[i] == '1':
            t += 1
        cnt[i] = t


    dp = [[0] * (1 + n) for _ in range(1 + n)]
    dp[0][0] = 1
    r = 0
    j = 0
    for i in range(n):
        while m > j:
            lj, rj = lst[j]
            if i >= lj:
                r = max(r, rj)
                j += 1
            else:
                break
        if i >= r:
            c = cnt[i]
            if 0 < c:
                dp[i + 1][cnt[i]] = (dp[i][c - 1] + dp[i][c]) % M
            else:
                dp[i + 1][0] = dp[i][0]
        else:
            for k in range(max(0, cnt[r] - r + i), min(i + 1, cnt[r]) + 1):
                if k > 0:
                    dp[i + 1][k] = (dp[i][k - 1] + dp[i][k]) % M
                else:
                    dp[i + 1][0] = dp[i][0]

    return dp[n][cnt[n - 1]]


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    s = input()
    lst = []
    for _ in range(m):
        l, r = input().split()
        l = int(l) - 1
        r = int(r) - 1
        lst.append((l, r))

    print(solve(n, m, s, lst))


def __starting_point():
    main()


__starting_point()
