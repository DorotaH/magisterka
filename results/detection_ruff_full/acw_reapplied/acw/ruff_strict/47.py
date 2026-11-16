def compute_Last_Digit(A, B):
	variable = 1
	if A == B:
		return 1
	if 5 <= (B - A):
		return 0
	for i in range(1 + A, B + 1):
		variable = (variable * (i % 10)) % 10
	return variable % 10
