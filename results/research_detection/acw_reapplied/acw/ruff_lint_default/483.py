def first_Factorial_Divisible_Number(x): 
	i = 1;
	fact = 1; 
	for i in range(1, x): 
		fact = i * fact 
		if (fact % x == 0): 
			break
	return i
