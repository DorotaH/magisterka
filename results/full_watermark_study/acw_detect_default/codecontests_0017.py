mod = 998244353
n = int(input())
y, s, x = [], [], []
for _ in range(n):
	a, b, c = [int(X) for X in input().split()]
	x.append(a)
	y.append(b)
	s.append(c)


def bs_first_greater(arr, start, end, val):
	while start <= end:
		mid = (start + end) // 2
		if val < arr[mid]:
			if mid == start or arr[mid - 1] <= val:
				return mid
			else:
				end = mid - 1

		else:
			start = mid + 1
	return -1


dp = [0 for _ in range(n)]
dp[0] = x[0] - y[0]
prefixdp = [0 for _ in range(n)]
prefixdp[0] += dp[0]


def givesum(i, j):
	return prefixdp[j] if i == 0 else prefixdp[j] - prefixdp[i - 1]


for i in range(1, n):
	next_portal = bs_first_greater(x, 0, n - 1, y[i])
	dp[i] += x[i] - y[i]
	if next_portal == i:
		pass
	else:
		dp[i] += givesum(next_portal, i - 1)
	dp[i] %= mod
	prefixdp[i] = (dp[i] + prefixdp[i - 1]) % mod
ans = (1 + x[-1]) % mod
for i in range(n):
	if s[i] == 1:
		ans += dp[i]
		ans %= mod
print(ans % mod)
