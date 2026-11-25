# Read input from standard input
S = input().strip()

# Check if there is a pair of stations operated by different companies
if 'AB' in S or 'BA' in S:
	print("Yes")
else:
	print("No")
