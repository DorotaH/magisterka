import sys
from collections import *

try:
    inp = raw_input
except:
    inp = input


def err(s):
    sys.stderr.write(f"{s}\n")


def ni():
    return int(inp())


def nl():
    return [int(_) for _ in inp().split()]


def solve():
    n, L, R = nl()
    L -= 1
    R -= 1
    SM = 0
    out = []
    for i in range(1, n):
        no = 2 * (n - i)
        if no + SM <= L:
            SM += no
            continue
        if R < SM:
            continue
        ARR = [i if j % 2 == 0 else i + j // 2 + 1 for j in range(no)]
        start = max(0, L - SM)
        end = R - SM + 1
        out.extend(ARR[start:end])
        SM += no
    if R == SM:
        out.append(1)
    print(" ".join(map(str, out)))


T = ni()
for _ in range(T):
    solve()
