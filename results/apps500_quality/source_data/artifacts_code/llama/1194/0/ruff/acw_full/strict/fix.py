

def read_ints():
	return list(map(int, input().split()))


def main():
	n = int(input())
	p = read_ints()
	q = read_ints()

	p = [n - 1 - i for i in range(n)]
	q = [n - 1 - i for i in range(n)]

	a = [0] * n
	for i in range(n):
		a[p[i]] = q[i]

	print(*a)


if __name__ == "__main__":
	main()
