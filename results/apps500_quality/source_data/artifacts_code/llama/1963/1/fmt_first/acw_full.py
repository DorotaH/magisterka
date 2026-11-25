import sys


def gcd(a, b):
	"""Compute the greatest common divisor of a and b"""
	while b:
		a, b = b, a % b
	return a


def find_max_r_l(a):
	"""Find the maximum r - l for all pairs (l, r) satisfying the conditions"""
	n = len(a)
	divisors = [[] for _ in range(10**6 + 1)]
	for i in range(1, 10**6 + 1):
		for j in range(i, 10**6 + 1, i):
			divisors[j].append(i)

	max_r_l = -1
	max_r = -1
	l_values = []
	for i in range(1, 1 + n):
		for d in divisors[a[i - 1]]:
			if a[i - 1] % d == 0:
				j = i
				while n >= j and a[j - 1] % d == 0:
					j += 1
				if j - i > max_r_l:
					max_r_l = j - i
					max_r = j - 1
					l_values = [i]
				elif j - i == max_r_l:
					l_values.append(i)
				i = j - 1

	return max_r_l, l_values


def main():
	n = int(sys.stdin.readline())
	a = [int(x) for x in sys.stdin.readline().split()]
	max_r_l, l_values = find_max_r_l(a)
	print(f"{len(l_values)} {max_r_l}")
	print(" ".join(map(str, l_values)))


if __name__ == "__main__":
	main()
