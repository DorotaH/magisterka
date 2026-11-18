fa = [1]
m = 251
P = 7 + 10**9
for i in range(1, 1 + m):
    fa.append(i * fa[-1] % P)
fainv = [pow(fa[m], P - 2, P)]
for i in range(1, 1 + m)[::-1]:
    fainv.append(i * fainv[-1] % P)
fainv = fainv[::-1]


def C(a, b):
    return fainv[a - b] * fa[a] * fainv[b] % P


N, K = list(map(int, input().split()))
poK = [1]
for _ in range(251):
    poK.append(poK[-1] * K % P)
poK1 = [1]
for _ in range(251):
    poK1.append((K - 1) * poK1[-1] % P)

dpC = [[C(i, j) for j in range(i + 1)] for i in range(N + 1)]
dpCpoK = [[C(i, j) * poK[j] % P for j in range(i + 1)] for i in range(N + 1)]

DP = [[0] * (N + 1) for _ in range(N + 1)]
DP[0][0] = 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1 + j):
            if k < j:
                DP[i][j] = (DP[i][j] + dpCpoK[j][k] * DP[i - 1][k]) % P
            else:
                DP[i][j] = (
                    DP[i][j] + dpC[j][k] * DP[i - 1][k] % P * (poK[k] - poK1[k])
                ) % P
    for j in range(1, N + 1):
        DP[i][j] = poK1[N - j] * DP[i][j] % P

print(DP[N][N])
