import fractions


def read_data():
    m=int(input())
    h1, a1=map(int, input().split())
    x1, y1=map(int, input().split())
    h2, a2=map(int, input().split())
    x2, y2=map(int, input().split())
    return  (m, h1, a1, x1, y1, h2, a2, x2, y2)


def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    t=0
    h1s, h2s = [-1] * m, [-1] * m
    h1s[h1]=0
    h2s[h2]=0
    t1, t2 = -1, -1
    while  h1 != a1 or  h2 != a2:
        t = t + 1
        h1=(x1 * h1+y1)%m
        h2=(x2 * h2+y2)%m
        if not (h1s[h1] >= 0 and t1 == -1):
            h1s[h1] = t
        else:
            t1 = h1s[h1]
            s1 = t - t1
            if t2 >= 0:
                break
        if not (h2s[h2] >= 0 and t2 == -1):
            h2s[h2] = t
        else:
            t2 = h2s[h2]
            s2 = t - t2
            if t1 >= 0:
                break
    if  h1 == a1 and  h2 == a2:
        return t
    return  retrieve(a1, a2, t1, s1, t2, s2, h1s, h2s)


def retrieve(a1, a2, t1, s1, t2, s2, h1s, h2s):
    u1, u2 = h1s[a1], h2s[a2]
    if  u1 == -1 or  u2 == -1:
        return -1
    if  u1 < t1:
        if not guess(h2s, u1, t2, s2, a2):
            return -1
        else:
            return u1
    if  u2 < t2:
        if not guess(h1s, u2, t1, s1, a1):
            return -1
        else:
            return u2
    return  find_time(u1, s1, u2, s2)


def guess(hs, u, t, s, a):
    if  u <= t:
        return hs[a] == u
    tt=t+(u - t) % s
    return  hs[a] == tt


def find_time(u1, s1, u2, s2):
    g=fractions.gcd(s1, s2)
    if  abs(u1 - u2) % g:
        return -1
    k1, k2=extended_euclid(s1, s2, u2-u1, g)
    b=s2//g
    return  (k1 % b) * s1+u1


def egcd(a, b):
    x, lastx = 0, 1
    y, lasty = 1, 0
    while  b:
        q=a//b
        a, b=b, a%b
        x, lastx=lastx-q * x, x
        y, lasty=lasty-q * y, y
    return  (lastx, lasty)


def extended_euclid(a, b, c, g):
    x, y=egcd(a, b)
    return  ((c // g) * x, (x // g) * y)


param=read_data()
print(solve(*param))
