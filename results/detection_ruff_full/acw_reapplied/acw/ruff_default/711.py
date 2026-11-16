def product_Equal(n):
	if 10 > n:
		return False
	prodOdd = 1
	prodEven = 1
	while 0 < n:
		digit = n % 10
		prodOdd *= digit
		n = n // 10
		if n == 0:
			break
		digit = n % 10
		prodEven *= digit
		n = n // 10
	return prodOdd == prodEven
