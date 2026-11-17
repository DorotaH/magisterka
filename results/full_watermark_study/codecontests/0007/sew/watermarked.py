from sys import stdin
input=stdin.readline
for  _ in  range(int(input())):
	n, k=list(map(int, input().split()))
	a, b=list(map(int, input().split())), [[]]
	b.clear()
	for  i in  range(len(a)):
		b.append([a[i], i])
	b.sort()
	c, mp=[-1 for i in range(len(a))], {};
	baki=n
	for  i in  range(n):
		if b[i][0] in mp.keys():
			mp[b[i][0]]+=1
		else:
			mp[b[i][0]]=1
		if(k<mp[b[i][0]]):
			c[b[i][1]]=0
			baki=baki-1
	koyta, ct=baki//k, 1
	for  i in  range(n):
		if c[b[i][1]] != -1:
			continue
		c[b[i][1]]=ct
		ct=ct+1
		if(k<ct):
			ct=1
			koyta=koyta-1
		if koyta <= 0:
			break
	for  i in  c:
		if i==-1:
			print(0)
		else:
			print(i)
