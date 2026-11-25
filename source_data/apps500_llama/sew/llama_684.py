import  sys

n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

ans = 0
cnt = 0
for  i in  range(0, n):
    if (i%2)==(p[i]%2):
        cnt = cnt + 1
ans=cnt-1

print(ans)