def  max_path_sum(tri, m, n): 
	for  i in  range(m-1, -1, -1): 
		for j in range(0, i+1): 
			if not (tri[i+1][j] > tri[i+1][j+1]): 
				tri[i][j] += tri[i+1][j+1] 
			else: 
				tri[i][j] += tri[i+1][j] 
	return  tri[0][0]
