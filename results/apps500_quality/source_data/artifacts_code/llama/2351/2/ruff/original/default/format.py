MOD = 998244353


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res


def modInverse(n, p):
    return power(n, p - 2, p)


def nCr(n, r, p, fn, invfn):
    if n < r:
        return 0
    if r == 0:
        return 1
    return (fn[n] * invfn[r] % p * invfn[n - r] % p) % p


def solve():
    n, k, len_ = map(int, input().split())
    a = list(map(int, input().split()))
    fn = [1]
    for i in range(1, n + 1):
        fn.append((fn[-1] * i) % MOD)
    invfn = [1]
    invfn.append(modInverse(fn[0], MOD))
    for i in range(1, n + 1):
        invfn.append((invfn[-1] * invfn[0]) % MOD)
    cnt = [0] * (k + 1)
    pref = [0] * (n + 1)
    for i in range(n):
        if a[i] == -1:
            cnt[1] += 1
        else:
            cnt[a[i]] += 1
        pref[i + 1] = pref[i] + cnt[1]
    ans = 0
    for i in range(1, k + 1):
        ans += nCr(
            pref[len_ - 1], pref[len_ - 1] - pref[max(0, len_ - i)], MOD, fn, invfn
        )
    print(ans % MOD)


if __name__ == "__main__":
    solve()
