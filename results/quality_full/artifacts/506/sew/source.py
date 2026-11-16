def permutation_coefficient(n, k): 
	P=[[0 for i in range(0, k + 1)] 
			for j in range(0, n + 1)] 
	for i in range(n + 1): 
		for j in range(min(i, k) + 1): 
			if (j == 0): 
				P[i][j] = 1
			else: 
				P[i][j] = P[i - 1][j] + ( 
						j * P[i - 1][j - 1]) 
			if (k > j): 
				P[i][1 + j] = 0
	return  P[n][k] 