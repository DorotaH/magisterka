import sys
from collections import deque

input = sys.stdin.readline

t = 1
t = int(input())
for  _ in  range(t):
    n=int(input())
    val, seg=set([0,2*10**5+1]), [(0,2*10**5+1)]
    for i in range(n):
        l,r = list(map(int,input().split()))
        val.add(l)
        val.add(r)
        seg.append((l,r))
    val=list(val)
    val.sort()
    comp={i:1+e for  e,i in  enumerate(val, 0)}
    for i in range(n+1):
        l,r = seg[i]
        seg[i] = (comp[l],comp[r])

    deg, out=[0]*(n+1), [[] for i in range(n+1)]
    for i in range(n+1):
        for  j in  range(1+i,1+n):
            l,r=seg[i]
            L,R=seg[j]
            if  L<=l and  r<=R:
                out[j].append(i)
                deg[i]+=1
            elif  l<=L and R<=r:
                out[i].append(j)
                deg[j] += 1

    ans=[0]
    deq=deque(ans)

    while  deq:
        v = deq.popleft()
        for  nv in  out[v]:
            deg[nv]-=1
            if  0==deg[nv]:
                deq.append(nv)
                ans.append(nv)

    dp=[0]*(1+n)
    def  solve(v):
        query = [[] for i in range(2*n+3)]
        for nv in out[v]:
            l,r=seg[nv]
            query[r].append((l,dp[nv]))
        subdp = [0] * (3+2*n)
        for i in range(1,3+2*n):
            res=subdp[i-1]
            for  l,val in  query[i]:
                test = subdp[l - 1] + val
                res = max(test,res)
            subdp[i]=res

        dp[v] = 1+subdp[-1]

    for v in ans[::-1]:
        solve(v)

    print(dp[0]-1)