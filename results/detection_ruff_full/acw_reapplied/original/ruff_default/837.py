def cube_Sum(n):
	sum = 0
	for i in range(0, n):
		sum += (i * 2 + 1) * (i * 2 + 1) * (i * 2 + 1)
	return sum
