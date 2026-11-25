MOD = 998244353
N = 10 + 1000


def qpow(a, b, p):
    res = 1
    a %= p
    while b:
        if b & 1:
            res = a * res % p
        a = a * a % p
        b >>= 1
    return res


def C(n, m):
    if m > n:
        return 0
    return (
        qpow(fac[m], MOD - 2, MOD) * fac[n] % MOD * qpow(fac[n - m], MOD - 2, MOD) % MOD
    )


fac = N * [1]
for i in range(1, N):
    fac[i] = fac[i - 1] * i % MOD

w, h = map(int, input().split())
dp = [[0] * (h + 1) for _ in range(1 + w)]
dp[0][0] = 1
for i in range(1, 1 + w):
    for j in range(1, h + 1):
        dp[i][j] = (
            (
                2 * dp[i - 1][j]
                + (
                    j - 1 >= i - 1
                    and (i % 2) * dp[i - 1][j - 1]
                    or (i % 2 == 0) * dp[i - 1][j - 1]
                )
            )
            % MOD
            * C(i + j - 2, i - 1)
            % MOD
        )

print(dp[w][h])
