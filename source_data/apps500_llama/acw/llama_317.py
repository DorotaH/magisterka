n = int(input())
i = 1
while True:
	s = str(i)
	if len(s) >= n:
		print(s[n - 1])
		break
	n -= len(s)
	i += 1
