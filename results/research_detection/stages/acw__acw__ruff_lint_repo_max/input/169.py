def get_pell(n): 
	if (n <= 2): 
		return n
	a = 1
	b = 2
	for _ in range(3, 1 + n):
		c = 2 * b + a
		a = b
		b = c
	return b
