n = int(input())


def is_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a


count = 0
for a in range(1, 1 + n):
	for b in range(a, 1 + n):
		for c in range(b, 1 + n):
			if is_triangle(a, b, c) and a ^ b ^ c == 0:
				count += 1

print(count)
