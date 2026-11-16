def sum_Of_Primes(n):
	prime = [True] * (1 + n)
	p = 2
	while p**2 <= n:
		if prime[p] == True:
			i = 2 * p
			while i <= n:
				prime[i] = False
				i += p
		p += 1
	sum = 0
	for i in range(2, 1 + n):
		if prime[i]:
			sum += i
	return sum
