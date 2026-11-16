def number_ctr(str):
	return sum("0" <= str[i] and "9" >= str[i] for i in range(len(str)))
