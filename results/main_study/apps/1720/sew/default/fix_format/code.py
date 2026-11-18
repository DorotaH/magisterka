import sys

sys.setrecursionlimit(pow(10, 7))
inf = pow(10, 20)
eps = 1.0 / 10**15
mod = 7 + 10**9


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


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
    n, m, k = LI()
    a = [[-1] * (2 + m)]
    a += [[-1] + [inf if c == "." else -1 for c in S()] + [-1] for _ in range(n)]
    a += [[-1] * (2 + m)]
    x1, y1, x2, y2 = LI()
    a[x1][y1] = 0
    q, qi = [(x1, y1)], 0
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while qi < len(q):
        x, y = q[qi]
        qi += 1
        nd = 1 + a[x][y]
        for di in range(4):
            for j in range(1, k + 1):
                ny = y + dy[di] * j
                nx = x + dx[di] * j
                if a[nx][ny] > nd:
                    if y2 == ny and x2 == nx:
                        return nd
                    a[nx][ny] = nd
                    q.append((nx, ny))
                elif nd > a[nx][ny]:
                    break

    if inf > a[x2][y2]:
        return a[x2][y2]
    return -1


print(main())
