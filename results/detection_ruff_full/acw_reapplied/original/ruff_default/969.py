def join_tuples(test_list):
	res = []
	for sub in test_list:
		if res and res[-1][0] == sub[0]:
			res[-1].extend(sub[1:])
		else:
			res.append(list(sub))
	return list(map(tuple, res))
