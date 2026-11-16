def overlapping(list1, list2):
	c = sum(1 for _ in list1)
	d = sum(1 for _ in list2)
	for i in range(0, c):
		for j in range(0, d):
			if list1[i] == list2[j]:
				return 1
	return 0
