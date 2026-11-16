def modular_inverse(arr, N, P):
	current_element = 0
	for i in range(N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = 1 + current_element
	return current_element
