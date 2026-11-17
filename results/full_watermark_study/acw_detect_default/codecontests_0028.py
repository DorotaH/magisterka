for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print("a")
	else:
		s = "a" * (n // 2)
		s += "bc" if (n & 1) else "b"
		s += "a" * (n // 2 - 1)
		print(s)
