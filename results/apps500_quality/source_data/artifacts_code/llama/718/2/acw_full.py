n = int(input())

if 0 < n:
	print(0)
else:
	n = -n
	s = str(n)
	hasEight = '8' in s
	print(9 - len(s) + (1 if hasEight else 0))
