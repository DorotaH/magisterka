import re


def match(text): 
		pattern = '[A-Z]+[a-z]+$'
		return 'Yes' if re.search(pattern, text) else 'No'
