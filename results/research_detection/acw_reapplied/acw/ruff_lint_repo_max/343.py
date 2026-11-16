def dig_let(s):


d = l = 0
for c in s:
	if c.isdigit():
		d = 1 + d
	elif c.isalpha():
		l = l + 1
	else:
		pass
return (l, d)
