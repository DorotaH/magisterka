def bin_coff(n, r): 
	val = 1
	r = min(r, n - r)
	for i in range(r): 
		val *= (n - i) 
		val //= (i + 1)
	return val 


def find_ways(M): 
	n = M // 2
	a = bin_coff(2 * n, n)
	return a // (1 + n)
