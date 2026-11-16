def is_undulating(n): 
	if (len(n) <= 2): 
		return False
	return all(n[i - 2] == n[i] for i in range(2, len(n)))