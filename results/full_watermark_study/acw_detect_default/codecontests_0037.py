import sys

input = sys.stdin.readline
INF = 7 + int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve():
	n = int(input())
	data = list(map(int, input().split()))
	remain = []
	final = [0] * n
	dp = [0] * n
	for i in range(n):
		now = i % 2
		if now == 0:
			remain.append((i, data[i]))
		else:
			k = data[i]
			while k and remain:
				idx, cost = remain.pop()
				if cost < k:
					dp[i] += cost
					k -= cost
					if idx > 0:
						dp[i] += final[idx - 1]
				else:
					if k == cost and idx > 0:
						final[i] = final[idx - 1] + 1
						dp[i] += final[idx - 1]
					else:
						final[i] = 1
					dp[i] += k
					cost -= k
					k = 0
					if cost:
						remain.append((idx, cost))
	print(sum(dp))


t = 1
while t:
	t -= 1
	solve()
