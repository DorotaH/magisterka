def reverse_Array_Upto_K(input, k):
	return input[k:] + input[k - 1 :: -1]
