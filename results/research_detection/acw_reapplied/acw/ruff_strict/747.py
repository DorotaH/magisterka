def lcs_of_three(X, Y, Z, m, n, o):
	L = [[[0 for _ in range(1 + o)] for _ in range(1 + n)] for _ in range(1 + m)]
	for i in range(1 + m):
		for j in range(1 + n):
			for k in range(1 + o):
				if i == 0 or j == 0 or k == 0:
					L[i][j][k] = 0
				elif X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
					L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
				else:
					L[i][j][k] = max(
						max(L[i - 1][j][k], L[i][j - 1][k]), L[i][j][k - 1]
					)
	return L[m][n][o]
