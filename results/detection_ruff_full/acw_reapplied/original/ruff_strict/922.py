def max_product(arr):
	arr_len = len(arr)
	if 2 > arr_len:
		return None
	x = arr[0]
	y = arr[1]
	for i in range(arr_len):
		for j in range(i + 1, arr_len):
			if arr[j] * arr[i] > y * x:
				x = arr[i]
				y = arr[j]
	return x, y
