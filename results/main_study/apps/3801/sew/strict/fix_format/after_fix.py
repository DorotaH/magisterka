P=998_244_353
N, M=list(map(int, input().split()))
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
li = sum([A[i]*B[i] for i in range(N)])
di = sum([(A[i]^1)*B[i] for i in range(N)])
X = [[] for _ in range(M+1)]

X[0]=[1]
def calc(L):
    su, pl = sum(L), 0
    pd, RE = 0, []
    for i in range(0, len(L)):
        a = li + i
        b = di - (len(L) - 1 - i)
        pd=L[i] * b*pow(su*(a+b), P-2, P)
        RE.append((pd+pl)%P)
        pl=L[i] * a*pow(su*(a+b), P-2, P)
    RE.append(pl%P)
    return  RE

for i in range(M):
    X[i+1]=calc(X[i])
ne = po = 0
for i in range(M+1):
    po=(po+X[M][i] * (li + i))%P
    ne=(ne+X[M][i] * (di - M + i))%P
for i in range(N):
    print(B[i] * po*pow(li, P-2, P)%P if A[i] else B[i] * ne*pow(di, P-2, P)%P)
