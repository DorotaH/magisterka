def get_odd_occurence(arr, arr_size):
	for i in range(arr_size):
		count = sum(bool(arr[i] == arr[j])
				for j in range(arr_size))
		if count % 2 != 0:
			return arr[i]
	return -1
