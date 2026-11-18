import math

a, b = [int(x) for x in input().split()]

area = a + b
t = int(math.sqrt(area))
sa = int(math.sqrt(a))
sb = int(math.sqrt(b))

D = []
DA = []
DB = []
for i in range(1, t + 1):
	if area % i == 0:
		D.append(i)
		if i * i != area:
			D.append(area // i)
for i in range(1, 1 + sa):
	if a % i == 0:
		DA.append(i)
		if i * i != a:
			DA.append(a // i)
for i in range(1, sb + 1):
	if b % i == 0:
		DB.append(i)
		if i * i != b:
			DB.append(b // i)
DA.sort()
DB.sort()
D.sort()

start = ((len(D) + 1) // 2) - 1
div = len(D)


def closestdiv(t, D):
	low = 0
	high = len(D) - 1
	while high - low > 1:
		guess = (high + low) // 2
		if t < D[guess]:
			high = guess
		else:
			low = guess
	return high if t >= D[high] else low


while start > -1:
	t = D[start]
	s = D[-start - 1]
	if DA[-closestdiv(t, DA) - 1] <= s or DB[-closestdiv(t, DB) - 1] <= s:
		print(t * 2 + 2 * s)
		break
	start -= 1
