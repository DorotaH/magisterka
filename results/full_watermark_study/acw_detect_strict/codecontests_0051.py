for _ in range(int(input())):
	k = int(input())
	sr = int((k - 1) ** 0.5)
	r = k - sr**2
	if sr >= r:
		print(r, sr + 1)
	else:
		print(sr + 1, sr + sr + 2 - r)
