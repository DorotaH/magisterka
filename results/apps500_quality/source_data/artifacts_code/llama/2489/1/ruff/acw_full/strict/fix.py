import math

N = int(input())
A = list(map(int, input().split()))

count = 0
primes = []

for i in range(2, 1 + int(math.sqrt(max(A)))):
	is_prime = all(i % j != 0 for j in range(2, 1 + int(math.sqrt(i))))
	if is_prime:
		primes.append(i)

for i in range(2, 1 + max(A)):
	is_prime = all(i % p != 0 for p in primes)
	if is_prime:
		count += 1
	else:
		for j in range(len(A)):
			if A[j] != i and i % A[j] == 0:
				break
		else:
			count += 1

print(count)
