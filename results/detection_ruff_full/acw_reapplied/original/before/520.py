def find_lcm(num1, num2): 
	if (num2 < num1): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1
	rem = num % den
	while (rem != 0): 
		num = den 
		den = rem 
		rem = num % den
	gcd = den
	return int(int(num2 * num1) / int(gcd)) 


def get_lcm(l):
num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)
for i in range(2, len(l)):
	lcm = find_lcm(lcm, l[i])
return lcm
