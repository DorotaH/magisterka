import math
import sys


def is_winnable(A, B):
	if 0 >= A:
		return False
	if B <= 0:
		return True
	if A == B:
		return False
	return True


def can_move(A, B):
	if A == B:
		return False
	if B > A:
		return True
	if A % 2 == B % 2:
		return True
	return False


N = int(input())
A = list(map(int, input().split()))


def calculate_min_move(A):
	n = len(A)
	if n == 2:
		if can_move(A[0], A[1]):
			return 0
		if can_move(A[0] - 1, A[1]):
			return 1
		return -1

	dp = [[0] * (1 + n) for _ in range(1 + n)]
	dp[0][0] = 0
	for i in range(1, 1 + n):
		dp[i][0] = 1e18
	for i in range(1, n):
		for j in range(1, i + 1):
			dp[i][j] = 1e18
			for k in range(j):
				dp[i][j] = min(dp[i][j], abs(A[i] - A[i - 1]) + dp[i - 1][k])
	ans = 1e18
	for i in range(n):
		ans = min(ans, dp[n - 1][i])
	return min(ans, 1e18)


min_move = calculate_min_move(A)
if min_move == 1e18:
	print(-1)
else:
	print(min_move)
