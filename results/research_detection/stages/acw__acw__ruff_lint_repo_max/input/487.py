def sort_tuple(tup): 
	lst = len(tup) 
	for i in range(0, lst): 
		for j in range(0, lst - i - 1): 
			if (tup[j][-1] > tup[1 + j][-1]): 
				temp = tup[j] 
				tup[j] = tup[1 + j] 
				tup[1 + j] = temp 
	return tup
