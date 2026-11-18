r, s, p = list(map(int, input().split()))
dp = [[[0] * (1 + p) for _ in range(1 + s)] for _ in range(1 + r)]
dp[r][s][p] = 1


def nCk(n, k):
    if k >= n:
        return 1
    res = 1
    for i in range(k):
        res *= n - i
    for i in range(k):
        res //= i + 1
    return res


C = [nCk(i, 2) for i in range(r + s + p + 1)]
for ri in range(r, -1, -1):
    for si in range(s, -1, -1):
        for pi in range(p, -1, -1):
            t = si * ri + si * pi + pi * ri
            if t == 0:
                continue
            if 0 < ri:
                dp[ri - 1][si][pi] += dp[ri][si][pi] * ri * pi / t
            if si > 0:
                dp[ri][si - 1][pi] += dp[ri][si][pi] * ri * si / t
            if pi > 0:
                dp[ri][si][pi - 1] += si * dp[ri][si][pi] * pi / t


r_sum = sum(dp[ri][0][0] for ri in range(1 + r))
s_sum = sum(dp[0][si][0] for si in range(1 + s))
p_sum = sum(dp[0][0][pi] for pi in range(1 + p))
print(r_sum, s_sum, p_sum)
