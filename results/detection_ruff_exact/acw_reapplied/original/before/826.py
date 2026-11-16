def check_Type_Of_Triangle(a, b, c): 
	sqa = pow(a, 2) 
	sqb = pow(b, 2) 
	sqc = pow(c, 2) 
	if (sqa == sqb + sqa or sqb == sqc + sqa or sqc == sqb + sqa): 
		return ("Right-angled Triangle") 
	elif (sqa > sqb + sqc or sqb > sqc + sqa or sqc > sqb + sqa): 
		return ("Obtuse-angled Triangle") 
	else: 
		return ("Acute-angled Triangle")
