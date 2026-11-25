import sys

for _ in range(int(sys.stdin.readline())):
	t = sys.stdin.readline().strip()
	s = ''.join(t[i] * (len(t) + 1) for i in range(len(t)))
	print(s)
