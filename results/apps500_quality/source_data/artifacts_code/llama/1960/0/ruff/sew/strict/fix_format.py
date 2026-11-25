import sys

input = sys.stdin.readline

n, a = int(input()), list(map(int, input().split()))

dp, lis = [1] * n, [1] * n

for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], 1 + dp[j])
            lis[i] = max(lis[i], lis[j])

mx, cnt = max(lis), [0, 0, 0]
for i in range(n):
    if lis[i] == 1:
        cnt[0] += 1
    elif mx == lis[i]:
        cnt[2] += 1
    else:
        cnt[1] += 1

for i in range(n):
    if mx == lis[i]:
        print("3", end="")
    elif cnt[1] > 0:
        cnt[1] -= 1
        print("2", end="")
    else:
        print("1", end="")
print()
