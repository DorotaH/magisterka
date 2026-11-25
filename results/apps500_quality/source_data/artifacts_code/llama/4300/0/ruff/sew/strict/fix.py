N = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(0, N):
    for  j in  range(1 + i, N):
        ans+=d[j] * d[i]

print(ans)
