import sys

input = sys.stdin.readline
mod = 998244353


def add(x, y):
    return (x + y) % mod


def mul(x, y):
    return (x * y) % mod


def power(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = mul(res, x)
        x = mul(x, x)
        y //= 2
    return res


def ncr(n, r):
    res = 1
    for i in range(r):
        res = mul(res, n - i)
    for i in range(1, r + 1):
        res = mul(res, power(i, mod - 2))
    return res


def solve():
    n, k = map(int, input().split())
    if n == 1:
        print(0)
        return

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 2
    dp[1][0] = 1

    for i in range(2, n + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = add(mul(dp[i - 1][j], 2), mod - dp[i - 1][j - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    ans = 0
    for i in range(1, n + 1):
        if i * (n - i) >= k:
            ans = add(ans, dp[i][i])

    print(ans)


solve()
