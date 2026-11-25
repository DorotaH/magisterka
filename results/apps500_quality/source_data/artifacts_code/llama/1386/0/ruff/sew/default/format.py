MOD, N = 998244353, 1000 + 10


def qpow(a, b, p):
    res = 1
    a %= p
    while b:
        if b & 1:
            res = a * res % p
        a = a * a % p
        b = b >> 1
    return res


def C(n, m):
    if m > n:
        return 0
    return (
        fac[n] * qpow(fac[m], MOD - 2, MOD) % MOD * qpow(fac[n - m], MOD - 2, MOD) % MOD
    )


fac = [1] * N
for i in range(1, N):
    fac[i] = i * fac[i - 1] % MOD

w, h = map(int, input().split())
dp = [[0] * (h + 1) for _ in range(w + 1)]
dp[0][0] = 1
for i in range(1, 1 + w):
    for j in range(1, h + 1):
        dp[i][j] = (
            (
                (dp[i - 1][j] * 2)
                + (
                    j - 1 >= i - 1
                    and dp[i - 1][j - 1] * (i % 2)
                    or dp[i - 1][j - 1] * (i % 2 == 0)
                )
            )
            % MOD
            * C(i + j - 2, i - 1)
            % MOD
        )

print(dp[w][h])
