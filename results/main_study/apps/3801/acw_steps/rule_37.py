P = 998244353
N, M = list(map(int, input().split()))
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
li = sum(B[i]*A[i] for i in range(N))
di = sum((A[i]^1)*B[i] for i in range(N))
X = [[] for _ in range(1+M)]

X[0] = [1]
def calc(L):
    su = sum(L)
    pl = 0
    pd = 0
    RE = []
    for i in range(len(L)):
        a = i + li
        b = di - (len(L) - 1 - i)
        pd = L[i] * b * pow(su*(a+b), P-2, P)
        RE.append((pd+pl)%P)
        pl = L[i] * a * pow(su*(a+b), P-2, P)
    RE.append(pl%P)
    return RE

for i in range(M):
    X[i+1] = calc(X[i])
ne = 0
po = 0
for i in range(1+M):
    po = (po + X[M][i] * (i + li)) % P
    ne = (ne + X[M][i] * (di - M + i)) % P
for i in range(N):
    print(B[i] * po * pow(li, P-2, P) % P if A[i] else ne * B[i] * pow(di, P-2, P) % P)
