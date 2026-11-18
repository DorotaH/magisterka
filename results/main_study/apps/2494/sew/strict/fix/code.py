from collections import deque

K = int(input())


INF = 10**9
res = [INF] * (K)
res[1] = 1
q = deque()
q.append(1)
while q:
    r=q.popleft()
    if  r==0:
        break
    nr=(r+1)%K
    if  res[nr]>res[r]:
        res[nr]=1+res[r]
        q.append(nr)
    nr=(r*10)%K
    if  res[nr]>res[r]:
        res[nr]=res[r]
        q.appendleft(nr)
print(res[0])
