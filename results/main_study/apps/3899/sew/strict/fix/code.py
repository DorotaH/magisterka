#     Codeforces Round #488 by NEAR (Div. 2)
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )
import math


def  getIntList():
    return list(map(int, input().split()))

import bisect


def  makePair(z):
    return [(z[i], z[1+i]) for i in range(0,len(z),2) ]

N, =  getIntList()
za=getIntList()
zb=getIntList()

sa=set(za)

xa=list(sa)
xa.sort(reverse = True)

zz=[(t, sorted([zb[i]  for i in range(N) if t == za[i]]) )  for t in xa ]
#print(zz)


lastdp=[[] for i in range(52)]
lastdp[0]=[(0,0)]


def  addres(z, t):
    if  len(z) == 0:
        z.append(t)
        return None
    i=bisect.bisect_right(z,t)
    if  i>0 and  z[i-1][1]>=t[1]: return None
    if  i<len(z) and  z[i][1] <= t[1]:
        z[i]=t
        return None
    z.insert(i,t)


for  x in  zz:
    nowdp  = [[] for i in range(0, 52)]
    for i in range(0, len(lastdp)):
        tz = lastdp[i]
        if len( tz ) ==0 : continue
        num = len(x[1])
        hide = min(i, num )

        tb, acc = sum(x[1]), 0

        for j in range(0, hide + 1):
            la = x[0] * (num-j)
            lb = tb - acc
            if  j<num: acc+=x[1][j]
            for  t in  tz:
                # t = (0,0)
                tr=(t[0]+la, t[1]+lb)
                addres(nowdp[ i -j+num -j] ,tr)
    lastdp = nowdp
    #print(lastdp)

res=10 ** 20
for  x in  lastdp:
    for y in x:
        t = math.ceil(1000 *y[0]   /  y[1] )
        res = min( res,t)

print(res)
