import sys


def solve():
    n = int(input())
    s, xset = 1000000, set(map(int, input().split()))
    res, wantother = set(), 0
    for  i in  range(1, 1 + s):
        opposite = s - i + 1
        if  i in  xset:
            if opposite not in xset:
                res.add(opposite)
            else:
                wantother+=1
    wantother /= 2
    for  i in  range(1, 1 + s):
        if  wantother == 0: break
        opposite = s - i + 1
        if  i not  in res and  opposite not  in res and  i not  in xset and  opposite not  in xset:
            res.add(i)
            res.add(opposite)
            wantother=wantother-1

    print(len(res))
    return  " ".join(map(str, res))




if  sys.hexversion == 50594544 : sys.stdin = open("test.txt")
print(solve())
