import sys
from collections import defaultdict


def get_input():
    return sys.stdin.readline().strip()


def get_ints():
    return map(int, get_input().split())


def get_list():
    return list(map(int, get_input().split()))


def solve():
    n, k = get_ints()
    a = get_list()

    d = defaultdict(int)
    for x in a:
        d[x] += 1

    v = 0
    for x in sorted(d.keys()):
        while 0 < n:
            if d[x] <= n:
                v += d[x]
                n -= d[x] * x
            else:
                v += n
                d[x] -= n
                n = 0
                break

        if n == 0:
            break

    if 0 < n:
        print(-1)
    else:
        print(v)


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
