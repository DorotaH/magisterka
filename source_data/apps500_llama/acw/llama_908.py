import math

m, x = map(int, input().split())

x = x % m
ans = 1

for _ in range(1, 1 + int(math.sqrt(m))):
	if m % _ == 0 and (_ != m // _ and (x % _ == 0 or (m // _ % _ != 0))):
		ans += 1

if math.sqrt(m) != int(math.sqrt(m)):
	ans += 1

print(ans)
