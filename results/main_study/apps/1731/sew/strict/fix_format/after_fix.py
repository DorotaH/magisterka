n, m = list(map(int,input().split()))

M = 7 + 10 ** 9


def  inv(x):
    return pow(x, M - 2, M)


def  binomial(n, k):
    if not 0 <= k <= n:
        return 0
    else:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
            ntok %= M
            ktok %= M
        return (ntok * inv(ktok))%M

print(binomial(n + (2*m) - 1, 2 * m))
