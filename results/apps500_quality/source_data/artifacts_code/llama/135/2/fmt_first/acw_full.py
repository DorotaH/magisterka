def check_remainders(n, k):
	seen = set()
	for i in range(1, k + 1):
		remainder = n % i
		if remainder in seen:
			return "No"
		seen.add(remainder)
	return "Yes"


n, k = map(int, input().split())
print(check_remainders(n, k))
