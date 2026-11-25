
n, c = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

dp = [0] * n
for  i in  range(1, n):
    dp[i] = dp[i - 1] + a[i - 1]

for  i in  range(1, n-1):
    dp[1 + i] = min(dp[i] + c + b[i], dp[i] + a[i])

for  i in  range(2, n):
    for  j in  range(i-1, 0, -1):
        dp[j]=min(dp[j], dp[i]+a[i-1]+a[i-2]+(c+b[i-1]+b[i-2] if  j>1 else 0))

print(' '.join(map(str, dp)))