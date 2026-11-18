import  sys
import  collections
rlines = sys.stdin.readlines()
lines = (l.strip() for  l in  rlines)

def eucycle(n,m,adj):
    diredges = []
    us = list(adj.keys())
    for  u in  us:
        while  adj[u]:
            v0=u
            v1=adj[v0].pop()
            adj[v1].remove(v0)
            diredges.append((v0,v1))
            while u != v1:
                v0=v1
                v1=adj[v0].pop()
                adj[v1].remove(v0)
                diredges.append((v0,v1))
    return  diredges

def solve(n,m,edges):
    adj = collections.defaultdict(set)
    diredges = []
    for  u,v in  edges:
        adj[u].add(v)
        adj[v].add(u)
    odds = set(u for u in adj if 1 == len(adj[u])%2)
    ans = n - len(odds)
    assert(0 == len(odds)%2)
    for  o in  odds:
        adj[1+n].add(o)
        adj[o].add(1+n)
    diredges = eucycle(1+n,m,adj)
    return  str(ans)+'\n'+'\n'.join(str(u)+' '+str(v) for  (u,v) in  diredges\
            if  u!=1+n and  v!=1+n)


t = int(next(lines))

for  ti in  range(0, t):
    n,m=[int(s) for  s in  next(lines).split()]
    edges=list()
    for  ei in  range(m):
        u,v=[int(s) for  s in  next(lines).split()]
        edges.append((u,v))
    #print(edges)
    print(solve(n,m,edges))

