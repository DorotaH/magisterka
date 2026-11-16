def round_num(n, m):
	a = m * (n // m)
	b = a + m
	return b if n - a > b - n else a
