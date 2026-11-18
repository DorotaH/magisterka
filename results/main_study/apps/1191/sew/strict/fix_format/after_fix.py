n,m=map(int, input().split())


class Knight:
	def  __init__(self, andis, p, c):
		self.p = int(p)
		self.c = int(c)
		self.andis = int(andis)
		self.ans = self.c

p, c = list(map(int, input().split())), list(map(int, input().split()))
x=list()
for i in range(0, n):
	x.append(Knight(i, p[i], c[i]))

x.sort(key=lambda x: x.p)
coins=list()
for i in range(0, n-1):
	if  len(coins) < m:
		coins.append(x[i].c)
		coins.sort()
	elif  len(coins) > 0:
		if  coins[0] < x[i].c:
			coins[0] = x[i].c
			coins.sort()
	x[1+i].ans+=sum(coins)

x.sort(key=lambda x:x.andis)
for k in x:
	print(k.ans, end=' ')




