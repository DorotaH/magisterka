import sys

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 7 + 10**9
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


N = inp()
aa = inpl()
Q = inp()

tmp = 0
ruiseki = [0]
for a in aa:
    tmp += a
    ruiseki.append(tmp)

for _ in range(Q):
    l, r = inpl()
    print((ruiseki[r] - ruiseki[l - 1]) // 10)
