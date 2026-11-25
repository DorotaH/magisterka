from math import comb

MOD = 1000000007


def count_ways(n, f):
	if f == 1:
		return 1
	if n == f:
		return 1
	if f == 2:
		return n - 1
	if f == n - 1:
		return n - 1
	if n % f == 0:
		return 0

	ways = 0
	for i in range(1, f):
		if n % i == 0:
			ways = (comb(n - 1, i - 1) + ways) % MOD
	return ways


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	q = int(data[0])
	results = []
	index = 1

	for _ in range(q):
		n = int(data[index])
		f = int(data[1 + index])
		index += 2
		results.append(count_ways(n, f))

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
