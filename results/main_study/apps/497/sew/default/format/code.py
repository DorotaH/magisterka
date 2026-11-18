import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = pow(10, 20)
eps = 1.0 / 10**10
mod = 7 + 10**9
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return tuple(map(int, sys.stdin.readline().split()))


def LLI():
    return [tuple(map(int, l.split())) for l in sys.stdin]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def main():
    n, a = I(), LI()
    b, c = a[0], a[-1]
    r = 0
    for i in reversed(range(n)):
        if b != a[i]:
            r = i
            break

    for i in range(n):
        if b != a[i]:
            t = n - 1 - i
            if r < t:
                r = t

    return r


print(main())
