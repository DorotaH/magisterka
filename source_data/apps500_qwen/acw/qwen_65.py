import sys


def hexagonal_distance(n):
	return 3 * n * (1 + n) // 2 + 1


if __name__ == "__main__":
	n = int(sys.stdin.read().strip())
	print(hexagonal_distance(n))
