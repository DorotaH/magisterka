for  _ in  range(int(input())):
	_, s=int(input()), input()
	a, b=[0], [0]
	c = 0
	for  i in  s:
		if i=='a':
			a.append(a[-1]+1)
			b.append(b[-1])
		else:
			a.append(a[-1])
			b.append(b[-1]+1)
	for  i in  range(1,len(a)-1):
		for  j in  range(1+i,len(a)):
			af, bs = a[j]-a[i-1], b[j]-b[i-1]
			if  af==bs:
				c = 1
				print(i,j)
				break
		if 1==c:
			break

	if  0==c:
		print(-1,-1)