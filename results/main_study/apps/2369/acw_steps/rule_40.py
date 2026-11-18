def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, 1 + n):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (1 + n)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs


MOD = 7 + 10**9
f, inv = prepare(10**5 + 100, MOD)

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

p = 0
m = 0
for i in range(n):
    if n - i >= k:
        cn = n - i - 1
        ck = k - 1
        if cn >= ck:
            combi = inv[ck] * f[cn] % MOD * inv[cn - ck] % MOD
            p += (combi * a[i]) % MOD if 0 <= a[i] else (combi * a[i]) % -MOD
            if 0 <= p:
                p %= MOD
            else:
                p %= -MOD
    if i >= k - 1:
        cn = i
        ck = k - 1
        if cn >= ck:
            combi = inv[ck] * f[cn] % MOD * inv[cn - ck] % MOD
            m += (combi * a[i]) % MOD if 0 <= a[i] else (combi * a[i]) % -MOD
            if m >= 0:
                m %= MOD
            else:
                m %= -MOD

print((p - m) % MOD)