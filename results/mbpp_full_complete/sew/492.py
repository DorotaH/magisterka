def binary_search(item_list,item):
	first=0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last) // 2
		if not item_list[mid] == item :
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
		else:
			found = True	
	return found
