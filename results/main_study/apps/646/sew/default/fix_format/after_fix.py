# import numpy as npy
import functools

n = int(input())
x = [0 for  i in  range(n+2)]
y, adj=[0 for i in range(n+2)], [[] for i in range(n+2)]
idx, idy=[], []
for i in range(n):
    x[i],y[i] = map(int,input().split())
    idx.append(i)
    idy.append(i)

def  cmpx(a,b):
    if  x[a]!=x[b]:
        if x[a]<x[b]:
            return -1
        else:
            return 1
    if  y[a]!=y[b]:
        if y[a]<y[b]:
            return -1
        else:
            return 1
    return  0
    
def  cmpy(a,b):
    if  y[a]!=y[b]:
        if y[a]<y[b]:
            return -1
        else:
            return 1
    if  x[a]!=x[b]:
        if x[a]<x[b]:
            return -1
        else:
            return 1
    return  0

idx = sorted(idx,key=functools.cmp_to_key(cmpx))
idy = sorted(idy,key=functools.cmp_to_key(cmpy))

# print(idx)
# print(idy)

def  disx(a,b):
    if  x[a]!=x[b]:
        return  1e18
    return  y[b] - y[a]
    
def  disy(a,b):
    if  y[a]!=y[b]:
        return  1e18
    return  x[b] - x[a]

l = 0
r, ans=2000000000, -1

while r>=l:
    # print(l,r)
    mid=(l+r)//2
    for  i in  range(n):
        adj[i] = list()
    for  i in  range(n-1):
        if  disx(idx[i],idx[1+i])<=mid:
            adj[idx[i]].append(idx[i+1])
            adj[idx[i+1]].append(idx[i])
            # print(idx[i],idx[i+1])
        if  disy(idy[i],idy[1+i])<=mid:
            adj[idy[i]].append(idy[i+1])
            adj[idy[i+1]].append(idy[i])
            # print(idy[i],idy[i+1])
    col, cur=[0 for i in range(n)], 0
    def  dfs(x):
        col[x]=cur
        for  i in  range(len(adj[x])):
            if  0==col[adj[x][i]]:
                dfs(adj[x][i])
    for  i in  range(n):
        if  0==col[i]:
            cur=cur+1
            dfs(i)
    ok=0
    if  cur>4:
        ok=0
    if  cur==1:
        ok=1
    if  cur==2:
        for i in range(n):
            for j in range(1+i,n):
                if  (col[j]!=col[i]):
                    d1, d2=abs(x[i]-x[j]), abs(y[i]-y[j])
                    if 0==d1 or 0==d2:
                        if  d1+d2<=mid*2:
                            ok=1
                    if d1<=mid and d2<=mid:
                        ok=1
    if  cur==3:
        for i in range(n-1):
            px, py=idx[i], idx[i+1]
            if  x[py]==x[px] and  col[py]!=col[px]:
                for  j in  range(n):
                    if  col[px]!=col[j] and  col[py]!=col[j]:
                        d1=abs(y[px]-y[j])
                        d2=abs(y[py]-y[j])
                        d3=abs(x[px]-x[j])
                        if  d1<=mid and  d2<=mid and  d3<=mid:
                            ok=1
        for i in range(n-1):
            px, py=idy[i], idy[i+1]
            if  y[py]==y[px] and  col[py]!=col[px]:
                for  j in  range(n):
                    if  col[px]!=col[j] and  col[py]!=col[j]:
                        d1=abs(x[px]-x[j])
                        d2=abs(x[py]-x[j])
                        d3=abs(y[px]-y[j])
                        if  d1<=mid and  d2<=mid and  d3<=mid:
                            ok=1
    if  cur==4:
        for i in range(n-1):
            px, py=idx[i], idx[i+1]
            if  x[py]==x[px] and  col[py]!=col[px]:
                for  j in  range(n-1):
                    pz=idy[j]
                    pw=idy[j+1]
                    if  y[pz]==y[pw] and  col[pz]!=col[pw]:
                        if  col[px]!=col[pz] and  col[py]!=col[pz]:
                            if col[px]!=col[pw] and col[py]!=col[pw]:
                                d1=abs(y[px]-y[pz])
                                d2=abs(y[py]-y[pz])
                                d3=abs(x[pz]-x[px])
                                d4=abs(x[pw]-x[px])
                                if mid>=d1 and mid>=d2 and mid>=d3 and mid>=d4:
                                    ok = 1
    if ok:
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)