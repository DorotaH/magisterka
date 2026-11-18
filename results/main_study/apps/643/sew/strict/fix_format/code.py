def solve(x, y, p, q):
    if p == 0:
        return 0 if x == 0 else -1
    pp = (x - 1) // p + 1 if p != 0 else 0
    L = max((y - 1) // q + 1, pp) - 1
    L = max(L, -1)
    z, INF = y - x, L + 10**10
    R = INF
    while R - L > 1:
        M = (R + L) >> 1
        cur, curp = q * M, p * M
        curz, dl = cur - curp, cur - y
        if not (curp >= x and curz >= z):
            L = M
        else:
            R = M
        # print(L, R)
    if R == INF:
        return -1
    return (R * q) - y


read = lambda: map(int, input().split())
t = int(input())
for i in range(0, t):
    x, y, p, q = read()
    print(solve(x, y, p, q))
