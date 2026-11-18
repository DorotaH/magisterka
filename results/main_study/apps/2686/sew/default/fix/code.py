from collections import deque
from sys import stdin, stdout

st=lambda:list(stdin.readline().strip())
li, mp=lambda:list(map(int,stdin.readline().split())), lambda:list(map(int,stdin.readline().split()))
inp, pr=lambda:int(stdin.readline()), lambda n: stdout.write(str(n)+"\n")

mod, INF=1000000007, float('inf')

def  solve():
    n,m=mp()
    d={i:[] for  i in  range(n+1)}
    for i in range(m):
        a,b = mp()
        d[a].append(b)
        d[b].append(a)
    x,y=mp()
    v=[False for i in range(n+1)]
    q=deque()
    q.append(x)
    dis=[INF for  i in  range(n+1)]
    dis[x]=0
    v[x]=True
    while q:
        a=q.popleft()
        for  i in  d[a]:
            if not v[i]:
                v[i]=True
                q.append(i)
                dis[i]=1+dis[a]
    if v[y]:
        pr(dis[y])
    else:
        pr(0)
                
        
        


for  _ in  range(1):
    solve()
