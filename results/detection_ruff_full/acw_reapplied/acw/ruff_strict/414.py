def overlapping(list1, list2):
	c = sum(1 for _ in list1)
	d = sum(1 for _ in list2)
	for i in range(c):
		for j in range(d):
			if list1[i] == list2[j]:
				return 1
	return 0
