t = int(input())

for _ in range(t):
	n = int(input())
	if n in [2, 3]:
		print(-1)
	else:
		p = list(range(1, 1 + n))
		for i in range(1, n - 1):
			if 2 > abs(p[i] - p[i - 1]) or abs(p[i] - p[i - 1]) > 4:
				print(-1)
				break
		else:
			for i in range(1, n - 1):
				if abs(p[i] - p[i - 1]) == 1:
					p[i] = p[i] + 3
			print(*p)
