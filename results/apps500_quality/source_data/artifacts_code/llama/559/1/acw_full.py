import sys


def read_ints():
	return list(map(int, input().split()))


def main():
	p = int(input())
	a = read_ints()

	b = [0] * p
	for i in range(p):
		b[i] = a[i] % p

	print(' '.join(map(str, b)))


if __name__ == "__main__":
	main()
