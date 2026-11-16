def rearrange_numbs(array_nums):
	return sorted(array_nums, key=lambda i: 0 if i == 0 else -1 / i)
