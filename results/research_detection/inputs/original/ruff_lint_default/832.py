import re


def extract_max(input): 
	numbers = re.findall(r'\d+',input) 
	numbers = map(int,numbers) 
	return max(numbers)