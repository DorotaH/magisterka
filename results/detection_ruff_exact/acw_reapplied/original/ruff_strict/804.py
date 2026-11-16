def is_Product_Even(arr, n):
	return any((arr[i] & 1) == 0 for i in range(n))
