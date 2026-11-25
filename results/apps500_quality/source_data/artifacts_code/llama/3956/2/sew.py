import sys
input=sys.stdin.readline


def modpow(a, n, mod):
    res=1
    while  n>0:
        if  n % 2 == 1:
            res = a * res % mod
        a=a*a%mod
        n //= 2
    return  res


def modinv(a, mod):
    return  modpow(a, mod-2, mod)

M=998244353

K, N=map(int, input().split())
K2, N1 = 2 * K, N + 1

dp=[0]*(1 + N)
dp[0]=1

for  _ in  range(0, K):
    ndp=[0]*(1 + N)
    for  i in  range(0, N + 1):
        for  j in  range(i, 1 + N):
            if  i + j <= N:
                ndp[i+j]+=dp[i] * dp[j]
    for  i in  range(0, N + 1):
        ndp[i] %= M
    dp=ndp

ans=[0]*K2
for  i in  range(1, K + 1):
    if not i % 2 == 0:
        ans[i] = modinv(N1, M) * dp[N] % M
    else:
        ans[i] = 0

for  i in  range(2, K):
    if not i % 2 == 0:
        ans[i] = modinv((N - i), M) * dp[N - i] % M
    else:
        ans[i] = 0

    if not i % 2 == 0:
        ans[i + 1] = modinv(N1, M) * (dp[N] - dp[N - i]) % M
    else:
        ans[i + 1] = 0

print(*ans)
