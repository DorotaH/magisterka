import  sys
input = sys.stdin.readline
def  solution():
    n,m = [int(x) for  x in  input().strip().split()]
    s, minx = input().strip(), 1
    maxx, miny = n, 1
    maxy = m
    res, updown = ['1','1'], 0
    leftright = 0
    for command in s:
        if (command=='U'): updown =updown -1
        if (command=='D'): updown =updown +1
        if (command=='L'): leftright=leftright-1
        if (command=='R'): leftright=leftright+1
        minx = max(minx, 1 - updown)
        maxx = min(maxx, n - updown)
        miny = max(miny, 1 - leftright)
        maxy = min(maxy, m - leftright)
        if (minx > maxx or miny > maxy): break
        res = [str(minx),str(miny)]
    print(' '.join(res))
for _ in range(int(input().strip())):
    solution()