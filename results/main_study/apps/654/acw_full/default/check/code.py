import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
mod = 7 + 10**9

ANS = [[0] * (1 + n) for _ in range(1 + n)]


def bra(x, y):
	if ANS[x][y] != 0:
		return ANS[x][y]

	if x == y == 0:
		ANS[x][y] = 0
		return 0

	if (y + x) % 2 == 1:
		A = 1
	else:
		A = 0

	if x == y or x != 0 and y == 0:
		ANS[x][y] = bra(x - 1, y) + A
		return ANS[x][y]

	elif x == 0:
		ANS[x][y] = A + bra(x, y - 1)
		return ANS[x][y]

	elif y > x:
		ANS[x][y] = bra(x - 1, y) + A + bra(x, y - 1)
		return ANS[x][y]


print(bra(n, n) % mod)
	
