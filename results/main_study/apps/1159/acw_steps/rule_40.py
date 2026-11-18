n = int(input())

def pr(x):
	return all(x % i != 0 for i in range(2, x))

e = [[i, (i + 1) % n] for i in range(n)]
x = n
u = 0
v = n // 2
while not pr(x):
	e += [[u, v]]
	x += 1
	u += 1
	v += 1

print(x)
for g in e:
	print(g[0] + 1, 1 + g[1])