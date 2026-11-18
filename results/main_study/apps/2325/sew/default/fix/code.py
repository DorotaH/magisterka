md = 10 ** 9 + 7


def cnk(n, k):
    if k>n//2:
        k = n - k
    ans = 1
    for i in range(n - k + 1, 1+n):
        ans = ans * i
    for i in range(2, 1+k):
        ans = ans // i
    ans = ans % md
    return  ans


def factor(n):
    pws, dv = [], 2
    lp = 0
    while  0 == n % dv:
        lp = lp + 1
        n = n // dv
    if lp:
        pws.append(lp)
    dv = 3
    while  n>1 and  dv*dv<=n:
        lp=0
        while n % dv == 0:
            lp = lp + 1
            n = n // dv
        if  lp:
            pws.append(lp)
        dv = dv + 2
    if n>1:
        pws.append(1)
    return  pws


def main():
    q = int(input())
    for __ in range(q):
        x, y = input().split()
        x, y = int(x), int(y)
        ans = pow(2, y - 1, md)
        for f in factor(x):
            cm=cnk(f+y-1, y-1)
            ans=(cm * ans)%md
        print(ans)


def __starting_point():
    main()
__starting_point()
