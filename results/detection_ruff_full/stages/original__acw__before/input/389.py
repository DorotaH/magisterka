def find_lucas(n): 
	if (n == 0): 
		return 2
	return 1 if (n == 1) else find_lucas(n - 1) + find_lucas(n - 2) 