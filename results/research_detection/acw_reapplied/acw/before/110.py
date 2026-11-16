def extract_missing(test_list, strt_val, stop_val):


res = []
for sub in test_list:
	if strt_val < sub[0]:
	res.append((strt_val, sub[0]))
	strt_val = sub[1]
	if stop_val > strt_val:
	res.append((strt_val, stop_val))
return (res)
