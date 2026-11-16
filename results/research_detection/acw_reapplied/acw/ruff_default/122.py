MAX = 3000


def smartNumber(n):
	primes = [0] * MAX
	result = []
	for i in range(2, MAX):
		if primes[i] == 0:
			primes[i] = 1
			j = i * 2
			while MAX > j:
				primes[j] -= 1
				if (3 + primes[j]) == 0:
					result.append(j)
				j = i + j
	result.sort()
	return result[n - 1]
