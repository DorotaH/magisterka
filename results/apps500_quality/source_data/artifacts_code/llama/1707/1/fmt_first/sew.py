import  sys
import  bisect

n = int(input())
a = sorted(list(map(int, input().split())))

ans = max_dist = 0
for i in range(0, n):
    for  j in  range(1 + i, n):
        dist=abs(a[j]-a[i])
        if  dist > max_dist:
            max_dist=dist
        if  a[i]+a[j]<=max_dist and  a[i]-a[j]<=max_dist:
            ans += 1

print(ans)