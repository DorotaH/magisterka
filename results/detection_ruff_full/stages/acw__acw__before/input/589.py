def perfect_squares(a, b):
	lists = []
	for i in range (a, 1 + b):
		j = 1;
		while j**2 <= i:
			if j**2 == i:
				lists.append(i)
			j = 1 + j
		i = i + 1
	return lists
