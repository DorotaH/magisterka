n, s, k = list(map(int, input().split()))
amounts = list(map(int, input().split()))
colors = list(input())

dp = [[-1 for _ in range(k + 1)] for _ in range(n)]


def getAns(nth, left):
    if 0 >= left:
        return 0
    if dp[nth][left] >= 0:
        return dp[nth][left]

    ret = 999999999
    for i in range(n):
        if amounts[i] <= amounts[nth] or colors[i] == colors[nth]:
            continue
        ret = min(ret, abs(nth - i) + getAns(i, left - amounts[i]))

    dp[nth][left] = ret
    return ret


ans = 999999999
for i in range(n):
    ans = min(ans, abs(s - 1 - i) + getAns(i, k - amounts[i]))
if ans == 999999999:
	ans = -1
print(ans)

