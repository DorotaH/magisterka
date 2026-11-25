import math

a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

min_h = float('inf')
max_h = 0
min_w = float('inf')
max_w = 0

for  ext in  extensions:
    min_h=min(min_h, ext)
    max_h=max(max_h, ext)

    min_w=min(min_w, 1/ext)
    max_w=max(max_w, 1/ext)

min_h, max_h = max(a, h*min_h), min(b, h*max_h)
min_w, max_w = max(a, min_w*w), min(b, max_w*w)

ans = float('inf')
for  i in  range(0, n+1):
    for j in range(n-i):
        if max_h/(extensions[j]*extensions[i])<=a and max_w/(extensions[j]*extensions[i])<=w and max_h/(extensions[j+1]*extensions[i+1])>=b and max_w/(extensions[j+1]*extensions[i+1])>=b:
            ans=min(ans, i+j)

if not ans == float('inf'):
    print(ans)
else:
    print(-1)
