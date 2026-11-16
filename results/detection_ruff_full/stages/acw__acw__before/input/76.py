def count_Squares(m, n):
	if (m > n):
		temp = m
		m = n
		n = temp
	return ((m * (1 + m) * (2 * m + 1) / 6 + (n - m) * m * (1 + m) / 2))
