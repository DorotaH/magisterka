from collections import defaultdict
m = 1000000007

f = [0] * 15001
f[0] = 1
for i in range(1, 15001): f[i] = (i * f[i - 1]) % m


def c(n, k): return (f[n] * pow((f[n - k] * f[k]) % m, m - 2, m)) % m


def prime(n):
	m = 1 + int(n ** 0.5)
	t = [1] * (1 + n)
	for i in range(3, m):
		if t[i]: t[i * i :: i * 2] = [0] * ((n - i * i) // (i * 2) + 1)
	return [2] + [i for i in range(3, 1 + n, 2) if t[i]]


p = prime(31650)
s = defaultdict(int)


def g(n):
	for j in p:
		while n % j == 0:
			n //= j
			s[j] += 1
		if j * j > n:
			s[n] += 1
			break


n = int(input()) - 1
a = list(map(int, input().split()))

for i in a: g(i)
if 1 in s: s.pop(1)

d = 1
for k in list(s.values()): d = (d * c(k + n, n)) % m
print(d)
