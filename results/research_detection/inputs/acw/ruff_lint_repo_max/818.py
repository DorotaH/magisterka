def lower_ctr(str):
	return sum(bool(str[i] >= 'a' and str[i] <= 'z')
			for i in range(len(str)))
