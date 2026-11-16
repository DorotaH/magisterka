import re

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check_email(email): 
	return "Valid Email" if (re.search(regex,email)) else "Invalid Email" 