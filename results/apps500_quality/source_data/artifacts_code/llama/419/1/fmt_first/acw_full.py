import sys

s = int(input(), 2)

count = 0
k = 0
while s:
	if s & (1 << k):
		count += 1
	k += 1
	s >>= 1

print(count)
