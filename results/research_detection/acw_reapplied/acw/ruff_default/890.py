def find_Extra(arr1, arr2, n):
	return next((i for i in range(0, n) if (arr1[i] != arr2[i])), n)
