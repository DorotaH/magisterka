MOD = 1000000007


def count_ways(n, f):
	if n == f:
		return 1
	if f > n:
		return 0
	if f == 1:
		return 1
	return (count_ways(n - 1, f - 1) + count_ways(n // 2, f - 1)) % MOD


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
