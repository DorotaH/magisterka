def extract_index_list(l1, l2, l3):
	return [m for m, n, o in zip(l1, l2, l3) if m == n == o]
