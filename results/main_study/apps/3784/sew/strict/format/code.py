mod = int(1e9 + 7)
n, m = map(int, input().split())
f, g = (
    [[0 for i in range(60)] for j in range(60)],
    [[0 for i in range(60)] for j in range(60)],
)
s, inv = [[0 for i in range(60)] for j in range(60)], [1]
f[0][0] = s[0][0] = 1


def pow(x, exp):
    res = 1
    for i in range(0, 31):
        if exp & 1:
            res = x * res % mod
        exp >>= 1
        if 0 == exp:
            break
        x = x * x % mod
    return res


for i in range(1, n + 1):
    inv.append(pow(i, mod - 2))

for node in range(1, n + 1):
    for cut in range(1, 1 + n):
        tmp = 0
        for ln in range(0, node):
            for lc in range(cut - 1, n + 1):
                if 0 == f[ln][lc]:
                    continue
                if lc == cut - 1:
                    tmp = (tmp + f[ln][lc] * s[node - ln - 1][cut - 1]) % mod
                else:
                    tmp = (tmp + f[ln][lc] * f[node - ln - 1][cut - 1]) % mod
        cnt = 1
        if 0 != tmp:
            cn, cc = 0, 0
            for i in range(1, 1 + n):
                cn += node
                cc += cut
                cnt = cnt * (tmp + i - 1) % mod * inv[i] % mod
                if n < cn or n < cc:
                    break
                for j in range(n - cn, -1, -1):
                    for k in range(n - cc, -1, -1):
                        if f[j][k] == 0:
                            continue
                        g[j + cn][k + cc] += f[j][k] * cnt
                        g[j + cn][k + cc] %= mod
            for i in range(0, n + 1):
                for j in range(0, n + 1):
                    f[i][j] = (f[i][j] + g[i][j]) % mod
                    g[i][j] = 0

    for cut in range(n, -1, -1):
        s[node][cut] = (s[node][cut + 1] + f[node][cut]) % mod
print(f[n][m - 1])
