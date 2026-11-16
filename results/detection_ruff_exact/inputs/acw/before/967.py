def check(string): 
if 5 <= len(set(string).intersection("AEIOUaeiou")): 
	return ('accepted') 
else: 
	return ("not accepted")
