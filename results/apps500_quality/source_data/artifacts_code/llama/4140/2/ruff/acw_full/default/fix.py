S = input()
n = len(S)

if n == 1:
	print(0)
else:
	painted = sum(bool(S[i] == S[i - 1])
			for i in range(1, n))
	print(painted)
