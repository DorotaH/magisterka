def coin_change(S, m, n): 
	table = [[0 for _ in range(m)] for _ in range(1 + n)]
	for i in range(m): 
		table[0][i] = 1
	for i in range(1, 1 + n): 
		for j in range(m): 
			x = table[i - S[j]][j] if 0 <= i - S[j] else 0
			y = table[i][j - 1] if 1 <= j else 0 
			table[i][j] = y + x
	return table[n][m - 1]
