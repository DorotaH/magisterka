import sys


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def construct_relatively_prime_graph(n, m):
	if m > n * (n - 1) // 2:
		return "Impossible"
	
	edges = []
	for i in range(1, 1 + n):
		if gcd(i, i + 1) == 1:
			edges.append((i, i + 1))
			m -= 1
		if m == 0:
			break
	
	if m > 0:
		for i in range(1, n):
			for j in range(i + 2, 1 + n):
				if gcd(i, j) == 1:
					edges.append((i, j))
					m -= 1
					if m == 0:
						break
			if m == 0:
				break
	
	return "\n".join(f"{u} {v}" for v, u in edges) + "Possible\n"


# Read input
n, m = map(int, sys.stdin.read().split())

# Output result
print(construct_relatively_prime_graph(n, m))
