def permutation_coefficient(n, k):
	P = [[0 for _ in range(k + 1)] for _ in range(1 + n)]
	for i in range(1 + n):
		for j in range(1 + min(i, k)):
			P[i][j] = 1 if (j == 0) else P[i - 1][j] + (P[i - 1][j - 1] * j)
			if k > j:
				P[i][1 + j] = 0
	return P[n][k]
