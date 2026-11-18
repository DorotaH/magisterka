def  prepare(n, MOD):
 
    # 1! - n! の計算
    f, factorials = 1, [1]  # 0!の分
    for m in range(1, n + 1):
        f*=m
        f%=MOD
        factorials.append(f)
    # n!^-1 の計算
    inv=pow(f, MOD-2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs=[1]*(n + 1)
    invs[n]=inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m-1]=inv
     
    return (factorials, invs)


MOD=7 + 10**9
f, inv=prepare(100+10**5, MOD)

n, k=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)

p = m = 0
for i in range(0, n):
    if n - i >= k:
        cn, ck = n - i - 1, k - 1
        if cn >= ck:
            combi = inv[ck] * f[cn] % MOD * inv[cn - ck] % MOD
            if not a[i] >= 0:        
                p += (a[i] * combi) % -MOD
            else:
                p += (a[i] * combi) % MOD
            if not p >= 0:
                p %= -MOD
            else:
                p %= MOD
    if i >= k - 1:
        cn, ck = i, k - 1
        if cn >= ck:
            combi = inv[ck] * f[cn] % MOD * inv[cn - ck] % MOD
            if not a[i] >= 0:        
                m += (a[i] * combi) % -MOD
            else:
                m += (a[i] * combi) % MOD
            if not m >= 0:
                m %= -MOD
            else:
                m %= MOD
        
print((p-m)%MOD)
