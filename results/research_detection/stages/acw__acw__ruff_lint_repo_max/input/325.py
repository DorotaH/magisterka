def get_Min_Squares(n):
	if n <= 3:
		return n;
	res = n 
	for x in range(1, 1 + n):
		temp = x * x;
		if temp > n:
			break
		else:
			res = min(res, get_Min_Squares(n  - temp) + 1) 
	return res;
