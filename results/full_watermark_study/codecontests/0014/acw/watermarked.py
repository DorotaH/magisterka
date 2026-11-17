def ch(x, y):
	if (y[0] < x[0] < y[1] and not (y[0] < x[1] < y[1])) or (y[0] < x[1] < y[1] and not (y[0] < x[0] < y[1])):
		return 1
	return 0
	

t = int(input())
for _ in range(t):
	n, k = [int(i) for i in input().split()]
	m = []
	use  = [0] * (2 * n + 1)
	for _ in range(k):
		l, r = [int(i) for i in input().split()]
		if l > r:
			l, r = r, l
		use[l] = 1
		use[r] = 1
		m.append([l, r])
	dontuse = [j for j in range(1, 2 * n + 1) if not (use[j])]
	ll = len(dontuse)
	for j in range(ll // 2):
		m.append([dontuse[j], dontuse[ll // 2 + j]])
	m.sort()
	ans = 0
	for j in range(n):
		for k in range(1 + j, n):
			if ch(m[j], m[k]):
				ans += 1
	print(ans)
		
		
		
	
	
