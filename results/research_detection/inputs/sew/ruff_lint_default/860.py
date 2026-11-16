import re

regex='[a-zA-z0-9]$'
def check_alphanumeric(string): 
	if not (re.search(regex, string)): 
		return ("Discard") 
	else: 
		return ("Accept") 
