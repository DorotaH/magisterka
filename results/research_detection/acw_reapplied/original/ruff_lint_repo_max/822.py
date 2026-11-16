import re


def pass_validity(p):
x = True
while x: 
if (6 <= len(p) and 12 >= len(p) and re.search("[a-z]", p)
	and re.search("[0-9]", p) and re.search("[A-Z]", p)
	and re.search("[$#@]", p) and not re.search("\s", p)):
return True
x = False
break
if x:
	return False
