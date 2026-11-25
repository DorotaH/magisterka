import sys

input = sys.stdin.read
data = input().split()

u = int(data[0])
v = int(data[1])

if u == 0 and v == 0:
	print(0)
elif u == 0 or v % u != 0:
	print(-1)
else:
	n = v // u
	if n == 1:
		print(2)
		print(u, v - u)
	else:
		print(n)
		for i in range(n):
			if i == n - 1:
				print(v)
			else:
				print(u)
