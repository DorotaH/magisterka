n = int(input())
b = list(map(int, input().split()))

a = [0] * n
x = 0

for i in range(n):
	if 0 <= b[i]:
		a[i] = x + b[i]
		x = a[i]
	else:
		a[i] = b[i]
		x = 0

print(" ".join(map(str, a)))
