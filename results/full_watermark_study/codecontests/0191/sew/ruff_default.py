import sys

I = lambda: [*map(int, sys.stdin.readline().split())]
N = 1 << 20
P = print
for _ in [0] * I()[0]:
    (n,) = I()
    p = I()
    D = [[-N, -N, N, N]]
    for i in range(1, n):
        a, b, c, d = [N] * 4
        w, x, y, z = D[i - 1]
        q, r = p[i], p[i - 1]
        if r < q:
            a = w
        elif w < q:
            c = r
        if w < -q:
            d = r
        a = min(a, x)
        if -r < -q:
            b = x
        elif x < -q:
            d = -r
        if y < q:
            a = min(a, r)
        elif r < q:
            c = y
        if z < q:
            a = min(a, -r)
        else:
            c = min(c, z)
        if z < -q:
            b = min(b, -r)
        elif -r < -q:
            d = min(d, z)
        D.append([a, b, c, d])
    if D[-1] == 4 * [N]:
        P("NO")
    else:
        P("YES")
        i, x, y = n, N - 1, N - 1
        while i > 0:
            i = i - 1
            a, b, c, d = D[i]
            v = p[i]
            if y >= a and x >= v:
                x, y = v, a
            elif b <= y and -v <= x:
                x, y = -v, b
                p[i] = -v
            elif c <= x and v <= y:
                x, y = c, v
            elif d <= x and -v <= y:
                x, y = d, -v
                p[i] = -v
        P(" ".join(map(str, p)))
