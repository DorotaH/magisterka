def dlog(x, n):
    bigMod = 5**n
    ans = [None, 0, 1, 3, 2][x % 5]
    val = 2**ans % bigMod
    mod, phi = 5, 4
    phiVal = 2**phi % bigMod
    for _ in range(2, 1 + n):
        nextMod = 5 * mod
        while val % nextMod != x % nextMod:
            val = val * phiVal % bigMod
            ans += phi
        phi *= 5
        phiVal = (
            phiVal
            * phiVal
            % bigMod
            * phiVal
            % bigMod
            * phiVal
            % bigMod
            * phiVal
            % bigMod
        )
        mod = nextMod
    return ans


def main():
    inp = input()
    n = len(inp)
    a = int(inp)
    for m in range(1 + n):
        l = a * 10**m
        x, mod = l, 2 ** (m + n)
        if x % mod != 0:
            x += mod - x % mod
        if x % 5 == 0:
            x += mod
        if x < l + 10**m:
            assert x % mod == 0 and x % 5 != 0
            x = x // mod
            mod = 5 ** (m + n)
            print(m + n + dlog(x % mod, m + n))
            return
    assert False


def __starting_point():
    cnt = int(input())
    for _ in range(cnt):
        main()


__starting_point()
