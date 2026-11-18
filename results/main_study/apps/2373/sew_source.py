import sys
input=sys.stdin.readline
from  collections import  deque

def  read():
    N, P = int(input().strip()), list(map(int, input().strip().split()))
    return N, P

def  solve(N, P):
    ans = 0
    p, q = deque(P), deque()
    q.append(p.popleft())
    for  i in  range(1, N):
        if not i == q[-1]:
            q.append(p.popleft())
        else:
            c = q.pop()
            q.append(p.popleft())
            q.append(c)
            ans += 1
    if  N == q[-1]:
        c = q.pop()
        d = q.pop()
        q.append(c)
        q.append(d)
        ans = ans + 1
    return ans

def  __starting_point():
    inputs = read()
    print((solve(*inputs)))

__starting_point()