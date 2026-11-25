import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = n * [1]
lis = n * [1]

for i in range(1, n):
	for j in range(i):
		if a[j] < a[i]:
			dp[i] = max(dp[i], dp[j] + 1)
			lis[i] = max(lis[i], lis[j])

mx = max(lis)
cnt = [0, 0, 0]
for i in range(n):
	if lis[i] == 1:
		cnt[0] += 1
	elif lis[i] == mx:
		cnt[2] += 1
	else:
		cnt[1] += 1

for i in range(n):
	if lis[i] == mx:
		print('3', end='')
	elif cnt[1] > 0:
		cnt[1] -= 1
		print('2', end='')
	else:
		print('1', end='')
print()
