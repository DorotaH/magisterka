def ziped(a):
	p=list()
	for i in a:
		x = int(i.split('-')[0])
		y = i.split('-')[1]
		if not (len(p) > 0 and p[-1][1] == y):
			p.append([x, y])
		else:
			p[-1][0] += x
	return p


def solve(a, b , c):
	ans=0
	if  len(b) == 1:
		for  token in  a:
			if c(token, b[0]):
				ans += token[0] - b[0][0] + 1
		return  ans

	if  len(b) == 2:
		for  i in  range(0, len(a) - 1):
			if c(a[i], b[0]) and c(a[i + 1], b[-1]):
				ans += 1
		return  ans

	v=b[1 : -1]+[[100500, '#']]+a
	p=[0]*len(v)
	for i in range(1, len(v)):
		j=p[i-1]
		while j > 0 and v[j] != v[i]:
			j = p[j - 1]
		if v[j] == v[i]:
			j += 1
		p[i]=j

	for i in range(len(v) - 1):
		if p[i]==len(b)-2 and c(v[i-p[i]], b[0]) and c(v[1 + i], b[-1]):
			ans += 1
	return ans

n, m=list(map(int, input().split()))
a = ziped(input().split())
b = ziped(input().split())
print(solve(a, b, lambda  x, y: y[1] == x[1] and  y[0] <= x[0]))
