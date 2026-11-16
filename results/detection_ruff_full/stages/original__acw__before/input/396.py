import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
	return "Valid" if (re.search(regex, string)) else "Invalid" 