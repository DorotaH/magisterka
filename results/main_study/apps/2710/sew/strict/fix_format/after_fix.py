#!/usr/bin/env python

class  ford_fulkerson:
    class  Edge:
        def __init__(self, to, cap, rev):
            self.to=to
            self.cap=cap
            self.rev=rev

        def __repr__(self):
            return  f"to : {self.to} cap : {self.cap} rev : {self. rev}"

    def __init__(self,V):
        self.V = V
        self.size = [0 for i in range(V)]
        self.G = [[] for i in range(V)]

    def add_edge(self, _from, to, cap):
        self.size[_from]
        self.G[_from].append(self.Edge(to, cap, self.size[to]))
        self.G[to].append(self.Edge(_from, 0, self.size[_from]))
        self.size[_from] += 1
        self.size[to] += 1

    def dfs(self, v, t, f):
        if v == t: return f
        self.used[v] = True
        for i in range(0, len(self.G[v])):
            edge = self.G[v][i]
            if self.used[edge.to] is False and edge.cap > 0:
                d = self.dfs(edge.to, t, f if edge.cap > f else edge.cap)
                if d > 0:
                    self.G[v][i].cap -= d
                    self.G[edge.to][edge.rev].cap += d
                    return  d
        return  0

    def max_flow(self, s, t):
        flow = 0
        while  1:
            self.used=[False for  _ in  range(0, self.V)]
            f=self.dfs(s, t, float('inf'))
            if  f == 0:
                return flow
            flow += f

N,M = list(map(int,input().split()))
A, B = list(map(int,input().split())), list(map(int,input().split()))

ff, S = ford_fulkerson(N*2+2), 1
T = 1 + N

for  i in  range(0, M):
    p,q=list(map(int, input().split()))
    ff.add_edge(p,T+q-1,10**9)
    ff.add_edge(q,T+p-1,10**9)

for  i in  range(0, N):
    ff.add_edge(1+i,T+i,10**9)
    ff.add_edge(0,S+i,A[i])
    ff.add_edge(T+i,1+2*N,B[i])

ans = [[0  for i in range(0, N)] for j in range(0, N)]
ff.max_flow(0,1+2*N)

for  i in  range(1,1+N):
    for v in ff.G[i]:
        if v.to != 0:
            ans[i-1][v.to-T]=ff.G[v.to][v.rev].cap

if M == 0:
    if A == B:
        print('YES')
        for i in range(N):
            for j in range(N):
                ans [i][j] = A[i] if i == j else 0
        for a in ans:
            print(' '.join(map(str,a)))
    else:
        print('NO')
else:
    if [sum([ans[i][j] for i in range(N)]) for j in range(N)] == B:
        print('YES')
        for a in ans:
            print(' '.join(map(str,a)))
    else:
        print('NO')
