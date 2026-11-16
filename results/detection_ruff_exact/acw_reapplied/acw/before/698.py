def sort_dict_item(test_dict):


return {
	key: test_dict[key]
	for key in sorted(test_dict.keys(), key=lambda ele: ele[0] * ele[1])
} 
