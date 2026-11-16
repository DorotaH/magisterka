def lower_ctr(str):
	return sum(bool("a" <= str[i] and str[i] <= "z")
		for i in range(len(str)))
