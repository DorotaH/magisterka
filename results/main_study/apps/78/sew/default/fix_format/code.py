from math import factorial


def lol(n):
    if n == 1:
        yield [0]
        yield [1]
    else:
        for p in lol(n - 1):
            p.append(0)
            yield p
            p[-1] = 1
            yield p
            p.pop()


def sp(g1, g2, g3, f):
    if g1 == 0:
        if g3 == g2:
            return 2
        elif 1 == abs(g2 - g3):
            return 1
        else:
            return 0
    elif g2 == 0:
        if g3 == g1:
            return 2
        elif abs(g1 - g3) == 1:
            return 1
        else:
            return 0
    elif g3 == 0:
        if g2 == g1:
            return 2
        elif abs(g2 - g1) == 1:
            return 1
        else:
            return 0
    else:
        if 1 == f:
            b, c = sp(g1, g2 - 1, g3, 2), sp(g1, g2, g3 - 1, 3)
            return b + c
        elif f == 2:
            a, c = sp(g1 - 1, g2, g3, 1), sp(g1, g2, g3 - 1, 3)
            return a + c
        elif f == 3:
            a, b = sp(g1 - 1, g2, g3, 1), sp(g1, g2 - 1, g3, 2)
            return a + b
        else:
            a, b = sp(g1 - 1, g2, g3, 1), sp(g1, g2 - 1, g3, 2)
            c = sp(g1, g2, g3 - 1, 3)
            return a + b + c


n, T = map(int, input().split())
S = []
cnt, M = 0, 10**9 + 7
for i in range(n):
    S.append(list(map(int, input().split())))
for p in lol(n):
    d = 0
    g1, g2, g3 = 0, 0, 0
    for i in range(n):
        if p[i]:
            d += S[i][0]
            if S[i][1] == 1:
                g1 += 1
            elif S[i][1] == 2:
                g2 = g2 + 1
            elif S[i][1] == 3:
                g3 = g3 + 1
    if T == d:
        cnt += factorial(g1) * factorial(g2) * factorial(g3) * sp(g1, g2, g3, 0)
        cnt %= M
print(cnt)
