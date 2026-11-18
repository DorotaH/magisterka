n=int(input())

def  pr(x):
	for  i in  range(2, x):
		if  x % i == 0:
			return False
	return  True

e=[]
for i in range(n):
	e += [[i, (1+i) % n]]
x=n
u, v = 0, n // 2
while not pr(x):
	e += [[u, v]]
	x = x + 1
	u = u + 1
	v = v + 1

print(x)
for g in e:
	print(1+g[0], 1+g[1])
