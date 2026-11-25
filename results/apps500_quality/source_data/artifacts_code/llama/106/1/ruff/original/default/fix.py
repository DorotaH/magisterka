import math

n, m, k = map(int, input().split())
a, b = map(int, input().split())

a -= 1
b -= 1

a_dist = (a % n) * m * k
a_dist += a // n * (m * k)

b_dist = (b % n) * m * k
b_dist += b // n * (m * k)

dist = abs(a_dist - b_dist)

up = (n - 1 - a % n) * 5
up += (a % n) * 5
down = (a % n) * 5
down += (n - 1 - a % n) * 5

left = (m - 1 - a // n % m) * 5
left += a // n % m * 5
right = (a // n % m) * 5
right += (m - 1 - a // n % m) * 5

if dist > n * m * k:
    ans = min(up + left + (b_dist - a_dist) % (n * m * k), down + right + (b_dist - a_dist) % (n * m * k))
else:
    ans = min(up + left + (b_dist - a_dist) % (n * m * k), down + right + (b_dist - a_dist) % (n * m * k), up + left + n * m * k + b_dist - a_dist, down + right + n * m * k + b_dist - a_dist)

print(ans + 10 * math.ceil((dist - 1) / 10))
