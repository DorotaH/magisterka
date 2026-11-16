def sort_tuple(tup): 
	n = len(tup) 
	for i in range(n): 
		for j in range(n - i - 1): 
			if tup[j][0] > tup[1 + j][0]: 
				tup[j], tup[1 + j] = tup[1 + j], tup[j] 
	return tup
