3

import sys

def solve(s, k):
    l = len(s)
    for i in reversed(range(l)):
        prev, z = s[max(i-2, 0):i], s[i] + 1
        while z in prev:
            z += 1
        if k <= z:
            continue
        # Gotcha!
        ret=s[:i]+[z]
        while len(ret) < l:
            prev, z = ret[max(len(ret)-2, 0):len(ret)], 0
            while  z in  prev:
                z = z + 1
            ret.append(z)
        return ret
    return None

def __starting_point():
    l, k = list(map(int, sys.stdin.readline().split()))
    s = []
    for c in sys.stdin.readline().strip():
        s.append(ord(c) - ord('a'))
    ans = solve(s, k)
    if not ans is None:
        print(''.join(chr(ord('a') + x) for x in ans))
    else:
        print('NO')

__starting_point()