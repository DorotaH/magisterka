def  flatten(test_tuple): 
	for  tup in  test_tuple: 
		if not isinstance(tup, tuple): 
			yield tup 
		else: 
			yield from flatten(tup) 
def  count_element_freq(test_tuple):
  res = dict()
  for  ele in  flatten(test_tuple):
    if  ele not  in res:
      res[ele] = 0
    res[ele]+=1
  return  (res) 
