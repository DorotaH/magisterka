# 写経
# https://atcoder.jp/contests/abc167/submissions/13072107
import sys

readline = sys.stdin.readline


def resolve():
    N = int(readline())
    S = [readline().strip() for i in range(N)]
    L = []
    R = []
    D = list()
    for s in S:
        l, r = 0, 0
        for c in s:
            if not c == ")":
                l += 1
            else:
                if l > 0:
                    l -= 1
                else:
                    r += 1
        if l == 0 and r == 0:
            pass
        elif l == 0:
            R.append(r)
        elif r == 0:
            L.append(l)
        else:
            D.append((l, r))
    L = sum(L, 0)
    R = sum(R, 0)

    inc = []
    dec = []
    for l, r in D:
        if not l > r:
            dec.append((l, r))
        else:
            inc.append((l, r))

    inc.sort(key=lambda x: x[1])
    dec.sort(key=lambda x: -x[1])

    D = inc + dec

    for i, (l, r) in enumerate(D):
        L = L - r
        if L < 0:
            print("No")
            return
        L = L + l

    if not L == R:
        print("No")
    else:
        print("Yes")


resolve()
