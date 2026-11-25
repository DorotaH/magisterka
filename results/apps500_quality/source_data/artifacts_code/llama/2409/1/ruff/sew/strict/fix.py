
def  can_koa_reach_island(n, k, l, d):
    p=[0]*(2 * k)
    for i in range(0, k):
        p[i] = -1
        p[(2 * k) - i - 1] = 1
    for i in range(0, k):
        p[i] = max(-l, min(p[i], l - d[i]))

    dp=[float('inf')]*(1 + n)
    dp[0]=0
    for i in range(1, n + 1):
        for  j in  range(0, k):
            if  d[i-1]+p[j]<=l:
                dp[i]=min(dp[i], dp[i - 1] + 1)
            if  k <= i and  d[i-1]+p[j]<=l:
                dp[i]=min(dp[i], dp[i - k] + 1)

    return dp[n]!=float('inf')

t = int(input())
for  _ in  range(t):
    n, k, l = map(int, input().split())
    d = list(map(int, input().split()))
    if not can_koa_reach_island(n, k, l, d):
        print("No")
    else:
        print("Yes")
