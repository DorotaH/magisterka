a = [int(x) for x in input().split()]
n = int(input())
a = [int(x) for x in input().split()]

b = 0
c = 0
for x in a:
	if x > 0:
		b += x
	else:
		c -= x

print(b - c)
