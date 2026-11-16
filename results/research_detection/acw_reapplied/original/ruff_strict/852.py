def remove_negs(num_list):
	for item in num_list:
		if 0 > item:
			num_list.remove(item)
	return num_list
