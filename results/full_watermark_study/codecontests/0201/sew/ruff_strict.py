import math
from sys import stdin

mod = 10**9 + 7


def inverse(n, mod):
    return pow(n, mod - 2, mod)


onehand = inverse(100, mod)

tt = int(stdin.readline())

ANS = []

for _ in range(0, tt):
    n, m, rb, cb, rd, cd, p = map(int, stdin.readline().split())
    p = p * onehand % mod

    # print (p)

    loop = 2 * (n - 1) * 2 * (m - 1) // math.gcd(2 * (n - 1), 2 * (m - 1))

    xmods = list()
    tx, diffx = rb, 1 if n != 1 else 0
    for i in range(loop):
        if tx == rd:
            xmods.append(i)
        if not (1 <= tx + diffx <= n):
            diffx *= -1
        tx += diffx

    ymods = list()
    ty, diffy = cb, 1 if m != 1 else 0
    for i in range(loop):
        if ty == cd:
            ymods.append(i)
        if not (1 <= ty + diffy <= m):
            diffy *= -1
        ty += diffy

    s = set(xmods)
    for i in ymods:
        s.add(i)
    lis = list(s)
    lis.sort()

    # print (lis,loop)
    lasta, lastb = 0, 1
    for i in range(len(lis) - 1, -1, -1):
        kai = loop - lis[i] if i == len(lis) - 1 else lis[i + 1] - lis[i]

        newa = ((1 - p) * (lasta + kai)) % mod
        newb = ((1 - p) * lastb) % mod

        # print (lis[i] , newa , newb , kai )

        if i == 0:
            ans = (newa + lis[0]) * inverse(1 - newb, mod)
            ANS.append(str(ans % mod))

        lasta = newa
        lastb = newb

# print ("\n".join(ANS))

print("\n".join(ANS))
