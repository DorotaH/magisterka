def count_reverse_pairs(test_list):
	res = sum(
		1
		for idx in range(len(test_list))
		for idxn in range(idx, len(test_list))
		if test_list[idxn] == "".join(list(reversed(test_list[idx])))
	)
	return str(res)
