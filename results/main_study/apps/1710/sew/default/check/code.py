#!/usr/bin/env python3

[n, k] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))

n1 = ais.count(1)

one_serie = []
for _ in range(n):
	one_serie.append(0)
for  i in  reversed(list(range(0, n))):
	if 1 == ais[i]:
		one_serie[i] = 1 + (0 if i == n - 1 else one_serie[i + 1])


n1_head = count = 0

for  i in  range(0, n):
	p = 1
	s = 0
	if i > 0 and 1 == ais[i - 1]:
		n1_head += 1
	n1_tail = n1 - n1_head
	j = i
	while j < n:
		if not ais[j] == 1:
			p *= ais[j]
			s += ais[j]
			if p == s * k:
				count += 1
			elif p > (s + n1_tail) * k:
				break
			j += 1
		else:
			if p % k == 0 and 1 <= p // k - s <= one_serie[j]:
				count += 1
			n1_tail -= one_serie[j]
			s += one_serie[j]
			j += one_serie[j]

print (count)
