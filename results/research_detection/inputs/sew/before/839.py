def sort_tuple(tup): 
	n=len(tup) 
	for  i in  range(0, n): 
		for j in range(0, n-i-1): 
			if tup[j][0]>tup[j + 1][0]: 
				tup[j], tup[j + 1] = tup[j + 1], tup[j] 
	return tup
