def check_greater(arr, number):


arr.sort()
if arr[-1] < number:
	return ('Yes, the entered number is greater than those in the array')
else:
	return ('No, entered number is less than those in the array')
