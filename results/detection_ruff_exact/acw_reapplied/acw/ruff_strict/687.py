def recur_gcd(a, b):
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	return 1 if low == 1 else recur_gcd(low, high % low)
