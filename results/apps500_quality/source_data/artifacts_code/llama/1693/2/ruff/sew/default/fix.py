
n = int(input())
m = list(map(int, input().split()))

dp = [0] * n
dp[0] = m[0]
for i in range(1, n):
    dp[i]=min(m[i], max(dp[i-1], m[i]))

ans = [0] * n
ans[0] = dp[0]

for i in range(1, n):
    ans[i]=min(m[i], max(ans[i-1], dp[i]))

print(*ans)