import math


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def make_graph(n, m):
	if m > (n - 2) * (n - 1) // 2:
		return "Impossible"

	edges = []
	v = 1
	e = 1
	while m >= e:
		for i in range(1, n - v):
			if gcd(v, i) == 1:
				edges.append((v, i))
				e += 1
				if m < e:
					return edges
		v += 1

	return edges


n, m = map(int, input().split())
print("Possible")
print(*make_graph(n, m), sep="\n")
