import sys
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get(x0, a, n):
    r = 0
    for i in range(n):
        p = (x0 - a[i].x)*(x0 - a[i].x) + 1.0*a[i].y*a[i].y
        p = p/2.0/a[i].y
        if 0 > p:
            p = -p
        r = max(r, p)
    return r

def main():
    n = int(input())
    pos, neg = False, False
    a = []
    for _ in range(n):
        x, y = map(int, input().split())
        t = Point(x, y)
        if 0 < t.y:
            pos = True
        else:
            neg = True
        a.append(t)
    if pos and neg:
        return -1
    if neg:
        for i in range(n):
            a[i].y = -a[i].y
    L, R = -1e8, 1e8
    for _ in range(120):
        x1 = L + (R-L)/3
        x2 = R - (R-L)/3
        if get(x2, a, n) > get(x1, a, n):
            R = x2
        else:
            L = x1
    return get(L, a, n)

def __starting_point():
    print(main())
__starting_point()