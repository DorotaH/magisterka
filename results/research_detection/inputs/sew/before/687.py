def recur_gcd(a, b):
	low, high = min(a, b), max(a, b)
	if  low == 0:
		return  high
	elif  1 == low:
		return  1
	else:
		return  recur_gcd(low, high%low)