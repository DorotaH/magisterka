t = int(input())

while t:
	num, k = [int(tok) for tok in input().split()]
	ans = 111111111111111
	num = str(num)
	n = len(num)
	s = set()
	for ch in num:
		s.add(ch)

	if k >= len(s):
		print(int(num))
	else:
		for ind in range(n):
			if num[ind] == "9":
				continue

			done = set()
			for i in range(ind):
				done.add(num[i])

			if k < len(done):
				continue

			elif len(done) == k:
				to_fill = None
				mi = "9"
				for el in done:
					mi = min(mi, el)
					if num[ind] < el:
						to_fill = el if to_fill is None else min(to_fill, el)
				if to_fill is not None:
					ans = min(ans, int(num[:ind] + to_fill + mi * (n - ind - 1)))

			else:
				mi = next((str(i) for i in range(9) if (num[ind] < str(i))), "9")
				done.add(mi)
				if len(done) == k:
					ans = min(ans, int(num[:ind] + mi + min(done) * (n - ind - 1)))
				else:
					ans = min(ans, int(num[:ind] + mi + "0" * (n - ind - 1)))

					# print(ind, ans)

		print(ans)

	t -= 1
