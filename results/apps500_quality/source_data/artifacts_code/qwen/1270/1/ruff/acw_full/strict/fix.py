def bachgold(n):
	if n <= 2:
		return n, [n]
	elif n % 2 == 0:
		return n // 2, (n // 2) * [2]
	else:
		return 1 + (n - 3) // 2, ((n - 3) // 2) * [2] + [3]


n = int(input().strip())
k, primes = bachgold(n)
print(k)
print(*primes)
