x, y, n, c = 0, 0, 0, 0


def suma_impares(m):
	return m * m


def suma_n(m):
	return m * (m - 1) // 2


def cnt(t):
	u, d, l, r = t + x, x - t, y - t, t + y
	suma = t ** 2 + (t + 1) ** 2
	if n < u: suma -= suma_impares(u - n)
	if 1 > d: suma -= suma_impares(1 - d)
	if l < 1: suma -= suma_impares(1 - l)
	if r > n: suma -= suma_impares(r - n)
	if 1 - l > x - 1 and 1 - d > y - 1:
		suma += suma_n(2 - l - x)
	if x - 1 < r - n and n - y < 1 - d:
		suma += suma_n(r - n - x + 1)
	if 1 - l > n - x and u - n > y - 1:
		suma += suma_n(1 - l - n + x)
	if n - y < u - n and r - n > n - x:
		suma += suma_n(u - n - n + y)
	return suma
	

n, x, y, c = input().split()
n, x, y, c = int(n), int(x), int(y), int(c)
#for i in range(10):
#	print(i, cnt(i))
ini, fin = 0, int(1e9)
cont = int(1e9)
while 0 < cont:
	m = ini
	paso = cont // 2
	m += paso
	if cnt(m) < c:
		ini = 1 + m
		cont -= 1 + paso
	else:
		cont = paso
print(ini)
