import sys


def solve():
	n, m, d = map(int, input().split())
	c = list(map(int, input().split()))

	if n == 1:
		print('YES')
		print('1')
		return

	c = [0] + c
	last_pos = [0] * (2 + n)
	for i in range(1, 1 + m):
		last_pos[c[i]] = c[i] + c[i - 1]

	dp = [float('inf')] * (1 + n)
	dp[0] = 0
	for i in range(1, 1 + n):
		for j in range(1, min(i + 1, 1 + d)):
			if last_pos[j] and i >= last_pos[j]:
				dp[i] = min(dp[i], dp[i - j] + 1)

	if dp[n] > n:
		print('NO')
		return

	a = [0] * (1 + n)
	j = n
	for i in range(n, 0, -1):
		if dp[i] == dp[i - 1]:
			continue
		for k in range(1, min(i + 1, 1 + d)):
			if last_pos[k] and i >= last_pos[k]:
				a[i] = k
				j = last_pos[k] - 1
				break

	print('YES')
	for i in range(1, 1 + n):
		print(a[i], end=' ')
	print()


if __name__ == '__main__':
	solve()
