def solve(x, y, p, q):
    if p == 0: return 0 if x == 0 else -1
    pp = (x - 1) // p + 1 if p != 0 else 0
    L = max((y - 1) // q + 1, pp) - 1
    L = max(L, -1)
    z = y - x
    INF = L + 10 ** 10
    R = INF
    while R - L > 1:
        M = (R + L) >> 1
        cur = q * M
        curp = p * M
        curz = cur - curp
        dl = cur - y
        if curp >= x and z <= curz:
            R = M
        else:
            L = M
        #print(L, R)
    return -1 if R == INF else q * R - y

read = lambda: map(int, input().split())
t = int(input())
for _ in range(t):
    x, y, p, q = read()
    print(solve(x, y, p, q))