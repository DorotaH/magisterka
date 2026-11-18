md = 7 + 10 ** 9


def cnk(n, k):
    if n // 2 < k:
        k = n - k
    ans = 1
    for i in range(n - k + 1, 1 + n):
        ans *= i
    for i in range(2, k + 1):
        ans //= i
    return ans % md


def factor(n):
    pws = []
    dv = 2
    lp = 0
    while n % dv == 0:
        lp += 1
        n //= dv
    if lp:
        pws.append(lp)
    dv = 3
    while n > 1 and dv**2 <= n:
        lp = 0
        while n % dv == 0:
            lp += 1
            n //= dv
        if lp:
            pws.append(lp)
        dv += 2
    if n > 1:
        pws.append(1)
    return pws


def main():
    q = int(input())
    for __ in range(q):
        x, y = input().split()
        x, y = int(x), int(y)
        ans = pow(2, y - 1, md)
        for f in factor(x):
            cm = cnk(y + f - 1, y - 1)
            ans = (cm * ans) % md
        print(ans)


def __starting_point():
    main()


__starting_point()
