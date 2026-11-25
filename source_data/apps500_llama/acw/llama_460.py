for _ in range(int(input())):
	t = input()
	period = next((i for i in range(1, len(t)) if t[i] != t[i % len(t)]), 1)
	s = ''.join(t[i % period] for i in range(len(t)))
	print(s)
