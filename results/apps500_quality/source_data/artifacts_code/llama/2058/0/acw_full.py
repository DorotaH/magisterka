from collections import deque
from sys import stdin, stdout


def solve(a, b):
	m, n = len(a), len(b)
	a = a + '0' + '0'
	b = '0' + b + '0'

	p = 0
	total = 0
	q = deque([0])
	for i in range(m, n):
		if b[i] == b[i - m]:
			p += 1
		else:
			p = 0
		q.append(p)
	
	for i in range(m, m + n):
		total += abs(a[i - m + 1] - b[i]) * q[i - m]

	print(total)


a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
solve(a, b)
