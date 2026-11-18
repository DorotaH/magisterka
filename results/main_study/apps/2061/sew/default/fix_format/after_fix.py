import sys

sys.setrecursionlimit(pow(10, 7))
inf, mod = 10**10, 10**9 + 7

def f():
    n,m,k = list(map(int, input().split()))
    a, g = [[inf]*(m+2)], []
    for _ in range(n):
        a.append([inf]+[_ for  _ in  input()]+[inf])
        g.append([False]*m)
    a.append([[inf] * (2+m)])

    c = 0
    for i in range(1,1+n):
        if  a[i][1] == '.':
            a[i][1]=-1
        if  a[i][-2] == '.':
            a[i][-2]=-1
    for j in range(1,1+m):
        if  a[1][j] == '.':
            a[1][j]=-1
        if  a[-2][j] == '.':
            a[-2][j]=-1
    def  ff(n1,n2):
        for  i in  range(1,n+1):
            for  j in  range(1,1+m):
                if a[i][j] == n1:
                    a[i][j]=n2
    ff('*', inf)

    for i in range(1,1+n):
        for j in range(1,m+1):
            if  a[i][j] == '.':
                mc=[inf]
                if  a[i - 1][j] != '.': mc.append(a[i-1][j])
                if  a[i+1][j] != '.': mc.append(a[1+i][j])
                if  a[i][j+1] != '.': mc.append(a[i][1+j])
                if  a[i][j - 1] != '.': mc.append(a[i][j-1])
                mm=min(mc)
                if not mm < inf:
                    a[i][j] = c
                    c += 1
                else:
                    a[i][j] = mm
                    for t in [_ for _ in mc if _ < inf and _ != mm]:
                        ff(t,mm)
    cnt = [0] * c
    for i in range(1,1+n):
        for j in range(1,m+1):
            if  -1 < a[i][j] < c:
                cnt[a[i][j]]+=1
    cnt2, r = [_ for _ in cnt if _ > 0], 0
    for _i in range(len(cnt2) - k):
        cnt2=[_ for  _ in  cnt if  _>0]
        mm=min(cnt2)
        ind=cnt.index(mm)
        cnt[ind]=0
        r+=mm
        for i in range(1,n+1):
            for  j in  range(1,1+m):
                if a[i][j] == ind:
                    a[i][j]='*'

    print(r)

    for i in range(1,1+n):
        s=''
        for j in range(1,m+1):
            c = a[i][j]
            if  c == '*':
                s+=c
            elif  c == inf:
                s += '*'
            else:
                s+='.'
        print(s)

f()