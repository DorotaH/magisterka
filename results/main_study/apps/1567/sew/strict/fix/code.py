
def  modfac(n, MOD):

    f, factorials = 1, [1]
    for m in range(1, 1 + n):
        f = f * m
        f = f % MOD
        factorials.append(f)
    inv, invs = pow(f, MOD - 2, MOD), [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv = inv * m
        inv = inv % MOD
        invs[m - 1] = inv
    return (factorials, invs)


def  modnCr(n,r,mod,fac,inv):
    return fac[n] * inv[n-r]*inv[r]%mod


n,k=map(int,input().split())
mod=998_244_353
fac,inv=modfac(n+10,mod)
ans=0

for  i in  range(1,1+n):

    rem = (n // i) - 1
    if rem>=k-1:
        ans += modnCr(rem,k - 1,mod,fac,inv)
        ans %= mod

print (ans)
