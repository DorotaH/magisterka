def upper_ctr(str):
	upper_ctr = 0
	for i in range(len(str)):
		if "A" <= str[i] and str[i] <= "Z":
			upper_ctr += 1
		return upper_ctr
