def kth_element(arr, n, k):


for i in range(n):
	for j in range(0, n - i - 1):
	if arr[j] > arr[1 + j]:
		arr[j], arr[1 + j] == arr[1 + j], arr[j]
return arr[k - 1]
