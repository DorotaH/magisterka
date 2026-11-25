import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])

if k == 0:
	print(n)
else:
	multiplier = 10**k
	if n % multiplier == 0:
		print(n)
	else:
		print((1 + n // multiplier) * multiplier)
