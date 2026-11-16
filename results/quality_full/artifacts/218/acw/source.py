import math   


def min_Operations(A, B):  
	if (B < A): 
		swap(A, B)  
	B = B // math.gcd(A, B);  
	return B - 1
