def sum_Square(n): 
	i = 1
	while i**2 <= n: 
		j = 1
		while j**2 <= n: 
			if j**2 + i**2 == n: 
				return True
			j = 1 + j
		i = i + 1
	return False
