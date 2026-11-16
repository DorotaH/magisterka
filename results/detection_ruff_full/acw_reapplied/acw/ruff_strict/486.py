def nCr(n, r):
	if n / 2 < r:
		r = n - r
	answer = 1
	for i in range(1, 1 + r):
		answer *= n - r + i
		answer /= i
	return answer


def binomial_probability(n, k, p):
	return nCr(n, k) * pow(p, k) * pow(1 - p, n - k)
