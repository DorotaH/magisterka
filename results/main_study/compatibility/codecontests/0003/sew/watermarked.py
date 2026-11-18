import  sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
a = [0]*(n+1)
ans = n
for i in range(0, m):
    u,v=list(map(int,input().split()))
    u=min(u,v)
    if  0==a[u]:
        ans-=1
    a[u]+=1

q = int(input())
for i in range(0, q):
    b=list(map(int,input().split()))
    if  1==b[0]:
        b[1]=min(b[1],b[2])
        if 0==a[b[1]]:
            ans-=1
        a[b[1]]+=1
    elif  b[0]==2:
        b[1] = min(b[1],b[2])
        a[b[1]] -= 1
        if 0==a[b[1]]:
            ans=ans+1
    else:
        print(ans)
        