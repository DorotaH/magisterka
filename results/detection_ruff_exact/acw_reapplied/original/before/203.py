def hamming_Distance(n1, n2) : 
	x = n1 ^ n2  
	setBits = 0
	while (0 < x) : 
		setBits += x & 1
		x >>= 1
	return setBits
