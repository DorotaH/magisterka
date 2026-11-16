def sequence(n): 
	if n in [1, 2]: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))