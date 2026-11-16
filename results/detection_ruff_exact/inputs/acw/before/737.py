import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'


def check_str(string): 
	return "Valid" if (re.search(regex, string)) else "Invalid"
