import  re 
regex='^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	if not (re.search(regex, string)): 
		return ("Invalid") 
	else: 
		return ("Valid") 
