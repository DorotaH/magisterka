

def solve():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))

	total_sum = sum(2**i * a[i] for i in range(1 + n))
	ways = 0

	for i in range(n):
		a_i = a[i]
		if total_sum - 2 * a_i <= 0:
			continue
		if k >= -a_i:
			ways += 1
		if k >= a_i:
			ways += 1

	print(ways)


if __name__ == "__main__":
	solve()
