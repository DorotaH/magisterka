from  itertools import  combinations
def sub_lists(my_list):
	subs=list()
	for i in range(len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs