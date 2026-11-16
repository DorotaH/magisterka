def sort_tuple(tup): 
	lst=len(tup) 
	for  i in  range(lst): 
		for j in range(lst-i-1): 
			if (tup[j][-1]>tup[j + 1][-1]): 
				temp = tup[j] 
				tup[j]= tup[j + 1] 
				tup[j + 1]= temp 
	return tup
