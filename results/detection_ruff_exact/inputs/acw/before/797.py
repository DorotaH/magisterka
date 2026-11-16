def sum_Odd(n): 
	terms = (1 + n) // 2
	return terms * terms  


def sum_in_Range(l, r): 
	return sum_Odd(r) - sum_Odd(l - 1)
