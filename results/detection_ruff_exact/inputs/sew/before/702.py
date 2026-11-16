def  find_ind(key, i, n, 
			k, arr):
	ind = -1
	start, end = i + 1, n - 1;
	while  (end > start):
		mid=int(start +
				((end - start) / 2))
		if not (arr[mid] - key <= k):
			end = mid
		else:
			ind = mid
			start = mid + 1
	return  ind
def  removals(arr, n, k):
	ans = n - 1
	arr.sort()
	for  i in  range(0, n):
		j = find_ind(arr[i], i, 
					n, k, arr)
		if (j!=-1):
			ans=min(ans, n -
						(j-i+1))
	return  ans