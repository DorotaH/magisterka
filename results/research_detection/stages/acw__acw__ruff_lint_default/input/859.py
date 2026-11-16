from itertools import combinations


def sub_lists(my_list):
	subs = []
	for i in range(1 + len(my_list)):
		temp = [list(x) for x in combinations(my_list, i)]
		if temp:
			subs.extend(temp)
	return subs
