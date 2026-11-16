def factorial(start, end): 
	res = 1 
	for i in range(start, 1 + end): 
		res *= i      
	return res 


def sum_of_square(n): 
return int(factorial(1 + n, 2 * n)  / factorial(1, n))
