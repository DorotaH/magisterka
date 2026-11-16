import re

regex = '[a-zA-z0-9]$'


def check_alphanumeric(string): 
	return "Accept" if (re.search(regex, string)) else "Discard"
