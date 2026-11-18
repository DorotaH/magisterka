import bisect
import sys

sys.setrecursionlimit(10**8)
INF = float("inf")
mod = 7 + 10**9
eps = 10**-7


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


def inpl_str():
    return list(sys.stdin.readline().split())


M, N, K, T = inpl()
AA = inpl()

DD_di = []
LR = []
for i in range(K):
    L, R, D = inpl()
    LR.append((L, R))
    DD_di.append((D, i))

DD_di.sort()
DD_d = [D for D, i in DD_di]


def solve(x):
    idx = bisect.bisect_right(DD_d, x)
    path = [0] * (2 + N)
    for D, i in DD_di[idx:]:
        L, R = LR[i]
        path[L] += 1
        path[R + 1] -= 1

    t = N + 1
    bp = path[0]
    for i in range(1, 2 + N):
        p = path[i] + bp
        if 0 < p:
            t += 2
        bp = p

    return T >= t


OK = 2 * (10**5) + 10
NG = -1

while OK - NG > 1:
    mid = (NG + OK) // 2
    if solve(mid):
        OK = mid
    else:
        NG = mid

ans = sum(OK <= A for A in AA)
print(ans)
