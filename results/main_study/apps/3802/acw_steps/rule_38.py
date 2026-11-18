# coding=utf-8
from functools import reduce

a = input()
b = input()
c = input()

alen = len(a)
blen = len(b)
clen = len(c)

kmpnext = [0]*(1+clen)
i = 1
j = 0
while i < clen:
	while 0 < j and c[i]!=c[j]:
		j = kmpnext[j]
	if c[i] == c[j]:
		j+=1
	kmpnext[i+1] = j
	i+=1
#print(kmpnext)

f = [[[0 for i in range(2+clen)] for i in range(2+blen)] for i in range(2+alen)]
g = [[[0 for i in range(2+clen)] for i in range(2+blen)] for i in range(2+alen)]
h = [[[0 for i in range(2+clen)] for i in range(2+blen)] for i in range(2+alen)]

f[0][0][0] = 0
g[0][0][0] = (-1,-1,-1)
h[0][0][0] = 1
m = (0,0,0)

for i in range(alen):
	for j in range(blen):
		for k in range(clen):
			if h[i][j][k] == 0:
				#print(i,j,k)
				continue
			if f[i+1][j][k] < f[i][j][k] or h[i+1][j][0] == 0:
				f[i+1][j][k] = f[i][j][k]
				g[i+1][j][k] = g[i][j][k]
				h[i+1][j][k] = 1
			if f[i][1+j][k] < f[i][j][k] or h[i][1+j][0] == 0:
				f[i][1+j][k] = f[i][j][k]
				g[i][1+j][k] = g[i][j][k]
				h[i][1+j][k] = 1

			if a[i] == b[j]:
				#print(i,j,a[i],b[j])
				kt = k
				while kt != 0 and a[i] != c[kt]:
					kt = kmpnext[kt]
				if a[i] == c[kt]:
					if f[i+1][1+j][kt+1] < 1 + f[i][j][k]:
						f[i+1][1+j][kt+1] = 1 + f[i][j][k]
						g[i+1][1+j][kt+1] = (i,j,k)
						h[i+1][1+j][kt+1] = 1
				else:
					if f[i+1][1+j][0] < 1 + f[i][j][k]:
						f[i+1][1+j][0] = 1 + f[i][j][k]
						g[i+1][1+j][0] = (i,j,k)
						h[i+1][1+j][0] = 1

			#print(i,j,k,f[i][j][k],g[i][j][k])

for i in range(alen+1):
	for j in range(blen+1):
		for k in range(clen):
			if f[m[0]][m[1]][m[2]] < f[i][j][k]:
				m = (i,j,k)
if f[m[0]][m[1]][m[2]] == 0:
	print(0)
else:
	ans = ""
	t = m
	t = g[t[0]][t[1]][t[2]]
	while t != (-1,-1,-1):
		ans = ans + a[t[0]]
		t = g[t[0]][t[1]][t[2]]
	print(ans)
