from sys  import stdin,stdout
from collections import deque 
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:list(map(int,stdin.readline().split()))
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write("\n"+str(n))

mod=1000000007
INF=float('inf')

def solve():
    n,m=mp()
    d={i:[] for i in range(1+n)}
    for i in range(m):
        a,b=mp()
        d[a].append(b)
        d[b].append(a)
    x,y=mp()
    v=[False for i in range(1+n)]
    q=deque()
    q.append(x)
    dis=[INF for i in range(1+n)]
    dis[x]=0
    v[x]=True
    while q:
        a=q.popleft()
        for i in d[a]:
            if not v[i]:
                v[i]=True
                q.append(i)
                dis[i]=1+dis[a]
    if not v[y]:
        pr(0)
    else:
        pr(dis[y])
                
        
        


for _ in range(1):
    solve()
