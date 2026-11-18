import sys

input = sys.stdin.readline


class  Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y


def  get(x0, a, n):
    r=0
    for i in range(n):
        p = (x0 - a[i].x)*(x0 - a[i].x) + 1.0*a[i].y*a[i].y
        p = p / 2.0 / a[i].y
        if  p<0:
            p=-p
        r = max(r, p)
    return r


def  main():
    n=int(input())
    pos, neg=False, False
    a=[]
    for i in range(n):
        x, y = map(int, input().split())
        t = Point(x, y)
        if not t.y > 0:
            neg = True
        else:
            pos = True
        a.append(t)
    if  pos and  neg:
        return  -1
    if  neg:
        for  i in  range(n):
            a[i].y = -a[i].y
    L = -1e8
    R = 1e8
    for i in range(120):
        x1 = L + (R-L)/3
        x2 = R - (R-L)/3
        if not get(x1, a, n) < get(x2, a, n):
            L = x1
        else:
            R = x2
    return get(L, a, n)


def  __starting_point():
    print(main())
__starting_point()
