import math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, 1 + n):
	for j in range(m - k + 1):
		is_match = all(math.gcd(i, l + j) == a[l] for l in range(k))
		if is_match:
			print("YES")
			exit()

print("NO")
