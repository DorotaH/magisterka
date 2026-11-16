def binomial_coeff(n, k): 
	C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
	for i in range(0, n + 1): 
		for j in range(0, min(i, k) + 1): 
			C[i][j] = 1 if j in [0, i] else (C[i - 1][j - 1] + C[i - 1][j])
	return C[n][k] 
def lobb_num(n, m): 
	return (((2 * m + 1) *
		binomial_coeff(2 * n, m + n)) 
					/ (m + n + 1))