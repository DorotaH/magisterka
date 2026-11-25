import math

n, m, k = map(int, input().split())
a, b = map(int, input().split())

a -= 1
b -= 1

a_dist = (a % n) * m * k
a_dist += a // n * (k * m)

b_dist = m * (b % n) * k
b_dist += b // n * (k * m)

dist = abs(a_dist - b_dist)

up = 5 * (n - 1 - a % n)
up += (a % n) * 5
down = (a % n) * 5
down += 5 * (n - 1 - a % n)

left = 5 * (m - 1 - a // n % m)
left += 5 * a // n % m
right = 5 * (a // n % m)
right += 5 * (m - 1 - a // n % m)

if dist > m * n * k:
	ans = min(
		up + left + (b_dist - a_dist) % (m * n * k),
		down + right + (b_dist - a_dist) % (m * n * k),
	)
else:
	ans = min(
		up + left + (b_dist - a_dist) % (m * n * k),
		down + right + (b_dist - a_dist) % (m * n * k),
		up + left + m * n * k + b_dist - a_dist,
		down + right + m * n * k + b_dist - a_dist,
	)

print(ans + 10 * math.ceil((dist - 1) / 10))
