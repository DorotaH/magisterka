a, b = list(map(int, input().split()))


def gcd(a, b):
    if 0 == b:
        return a
    return gcd(b, a % b)


def burn(n):
    c = 0
    while 0 == n % 2:
        c += 1
        n //= 2
    while 0 == n % 3:
        c += 1
        n //= 3
    while 0 == n % 5:
        c += 1
        n //= 5
    return [c, n]


if a == b:
    print(0)
else:
    g = gcd(a, b)
    c = a // g
    d = b // g
    l1 = burn(c)
    l2 = burn(d)
    if l1[1] == 1 and l2[1] == 1:
        print(l1[0] + l2[0])
    else:
        print(-1)
