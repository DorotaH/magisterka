def frequency(a, x):
	return sum(bool(i == x)
		for i in a)
