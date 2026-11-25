import sys


def solve():
	n = int(input())
	x, y = map(int, input().split())

	if n in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
		x, y = n - x + 1, n - y + 1
		if (y + x) % 2 == 0:
			print('White')
		else:
			print('Black')
	else:
		print('White' if (y + x) % 2 == 0 else 'Black')


if __name__ == '__main__':
	solve()
