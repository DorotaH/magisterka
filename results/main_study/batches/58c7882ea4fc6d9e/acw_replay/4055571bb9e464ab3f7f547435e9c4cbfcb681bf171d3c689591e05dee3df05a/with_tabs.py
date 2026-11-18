n = int(input())
C = [0] + list(map(int, input().split()))

A = [C[i] for i in range(1, 1 + n) if C[i] != C[i - 1]]
L = len(A)
DP = [[[0] * L for _ in range(L)] for _ in range(2)]
# 左の色に揃える or 右の色に揃える,左からi～j番目を


def color(r, i, j):  # i<j
	if r == 1:
		DP[r][i][j] = (
			min(DP[0][i][j - 1], DP[1][i][j - 1] + 1)
			if A[i] == A[j]
			else min(1 + DP[0][i][j - 1], DP[1][i][j - 1] + 1)
		)
	elif A[i] == A[j]:
		DP[r][i][j] = min(DP[1][i + 1][j], DP[0][i + 1][j] + 1)
	else:
		DP[r][i][j] = min(DP[1][i + 1][j] + 1, DP[0][i + 1][j] + 1)


for i in range(1, L):
	for j in range(L - i):
		color(0, j, i + j)
		color(1, j, i + j)

	# print(DP)

print(min(DP[0][0][L - 1], DP[1][0][L - 1]))
