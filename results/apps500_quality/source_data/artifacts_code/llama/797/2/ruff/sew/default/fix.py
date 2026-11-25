
n, m, a, b=map(int, input().split())
g0, x, y, z=map(int, input().split())

g=[0]*(m * n)
g[0]=g0

for i in range(1, m * n):
    g[i]=(g[i - 1] * x+y)%z

heights=[0]*(m + 1)
for j in range(m):
    min_height=g[j]
    for  i in  range(j, n * m, m):
        min_height = min(min_height, g[i])
    heights[j + 1]=min_height

prefix_heights=[0]*(m + 1)
for i in range(m):
    prefix_heights[i + 1]=prefix_heights[i]+heights[i + 1]

ans=0
for i in range(a):
    min_height=float('inf')
    for  j in  range(b):
        min_height = min(min_height, heights[j + (i * m)])
    ans+=min_height

    for  k in  range(1 + i, a):
        min_height = float('inf')
        for  j in  range(b):
            min_height=min(min_height, heights[j+(k * m)])
        ans += min_height

    for  k in  range(i, a):
        ans -= (prefix_heights[(1 + k) * m] - prefix_heights[m * i])

print(ans)