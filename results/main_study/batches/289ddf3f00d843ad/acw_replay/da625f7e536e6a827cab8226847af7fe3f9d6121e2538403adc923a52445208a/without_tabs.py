mod = int(1e9 + 7)
n, m = map(int, input().split())
f = [[0 for _ in range(60)] for _ in range(60)]
g = [[0 for _ in range(60)] for _ in range(60)]
s = [[0 for i in range(60)] for _ in range(60)]
inv = [ 1 ]
f[0][0] = s[0][0] = 1


def pow(x, exp):
    res = 1
    for _ in range(31):
        if exp & 1 : res = res * x % mod
        exp >>= 1
        if exp == 0 : break
        x = x * x % mod
    return res


for i in range(1, 1 + n) :
    inv.append( pow(i, mod - 2) )

for node in range(1, 1 + n) :
    for cut in range(1, 1 + n) :
        tmp = 0
        for ln in range(node) :
            for lc in range(cut - 1, 1 + n) :
                if f[ln][lc] == 0 : continue
                if lc == cut - 1 :
                    tmp = ( tmp + f[ln][lc] * s[node - ln - 1][cut - 1] ) % mod
                else :
                    tmp = ( tmp + f[node - ln - 1][cut - 1] * f[ln][lc] ) % mod
        cnt = 1
        if tmp != 0 :
            cn, cc = 0, 0
            for i in range(1, 1 + n) :
                cn += node
                cc += cut
                cnt = cnt * (i + tmp - 1) % mod * inv[i] % mod
                if cn > n or cc > n : break
                for j in range(n - cn, -1, -1) :
                    for k in range(n - cc, -1, -1) :
                        if f[j][k] == 0 : continue
                        g[cn + j][k + cc] += cnt * f[j][k]
                        g[cn + j][k + cc] %= mod
            for i in range(1 + n) :
                for j in range(1 + n) :
                    f[i][j] = (g[i][j] + f[i][j]) % mod
                    g[i][j] = 0
            
    for cut in range(n, -1, -1) :
        s[node][cut] = ( s[node][1 + cut] + f[node][cut] ) % mod
print(f[n][m - 1])
