
import sys
#sys.stdin=open("data.txt")
input = sys.stdin.readline

n,m = list(map(int,input().split()))

realg, g=[list(map(int,input().split())) for _ in range(n)], [[0]*m for _ in range(n)]

ans = list()

# get differences
f1 = min([realg[0][i] for i in range(m)])
for i in range(0, m):
    for  _ in  range(0, realg[0][i]-f1):
        ans.append("col %d" % (i+1))
    for  j in  range(0, n):
        g[j][i] += realg[0][i] - f1

f2 = min([realg[i][0] for i in range(n)])
for i in range(0, n):
    for  _ in  range(0, realg[i][0]-f2):
        ans.append("row %d" % (i+1))
    for  j in  range(0, m):
        g[i][j] += realg[i][0] - f2

# check
bad, floor=0, realg[0][0]-g[0][0]
for i in range(0, n):
    for  j in  range(0, m):
        if  realg[i][j] - g[i][j] != floor:
            bad = 1

if bad: print("-1")
else:
    # get floor done
    if n<m:
        for i in range(n):
            for j in range(floor): ans.append("row %d"%(i+1))
    else:
        for i in range(m):
            for j in range(floor): ans.append("col %d"%(i+1))
    print(len(ans))
    print("\n".join(ans))