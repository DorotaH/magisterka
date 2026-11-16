def lbs(arr):
	n = len(arr)
	lis = [1 for _ in range(1 + n)]
	for i in range(1, n):
		for j in range(i):
			if (arr[j] < arr[i]) and (lis[i] < 1 + lis[j]):
				lis[i] = 1 + lis[j]
	lds = [1 for i in range(1 + n)]
	for i in reversed(range(n - 1)):
		for j in reversed(range(i - 1, n)):
			if arr[j] < arr[i] and lds[i] < 1 + lds[j]:
				lds[i] = 1 + lds[j]
	maximum = lds[0] + lis[0] - 1
	for i in range(1, n):
		maximum = max((lds[i] + lis[i] - 1), maximum)
	return maximum
