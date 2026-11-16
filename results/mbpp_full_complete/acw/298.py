def intersection_nested_lists(l1, l2):
	return [[n for n in lst if n in l1] for lst in l2]
