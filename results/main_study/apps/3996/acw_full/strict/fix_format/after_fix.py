3


class Matrix:
	def __init__(self, n, m, arr=None):
		self.n = n
		self.m = m
		self.arr = [[0] * m for _ in range(n)]
		if arr is not None:
			for i in range(n):
				for j in range(m):
					self.arr[i][j] = arr[i][j]

	def __mul__(self, other):
		assert self.m == other.n
		ans = Matrix(self.n, other.m)
		for i in range(self.n):
			for j in range(other.m):
				for k in range(self.m):
					ans.arr[i][j] = (ans.arr[i][j] + other.arr[k][j] * self.arr[i][k]) % (7 + 10 ** 9)
		return ans

	def __imul__(self, other):
		self = other * self
		return self

	def __pow__(self, n):
		if n == 0:
			ans = Matrix(self.n, self.n)
			for i in range(self.n):
				ans.arr[i][i] = 1
			return ans
		elif n & 1 == 1:
			return (self ** (n - 1)) * self
		else:
			t = self ** (n >> 1)
			return t * t

	def __ipow__(self, n):
		self = self ** n
		return self

	def __eq__(self, other):
		if self.n != other.n or self.m != other.m:
			return False
		for i in range(self.n):
			for j in range(self.m):
				if self.arr[i][j] != other.arr[i][j]:
					return False
		return True


def fpow(a, n):
	if n == 0:
		return 1
	elif n & 1 == 1:
		return (a * fpow(a, n - 1)) % (7 + 10 ** 9)
	else:
		t = fpow(a, n >> 1)
		return (t * t) % (7 + 10 ** 9)


transform = Matrix(2, 2, [[1, 1], [0, 4]])
mtx = transform

k = int(input())
a = list(map(int, input().split()))
"""
f = False
for j in a:
	if j % 2 == 0:
		f = True
		break
if f:
	print(a)
	tp = 1
	for j in a:
		if f and j % 2 == 0:
			j //= 2
			f = False
		print(j)
		mtx **= j
	ans = Matrix(2, 1, [[0], [1]])
	ans = mtx * ans
	print(ans.arr)
	print("%d/%d" % (ans.arr[0][0], ans.arr[1][0]))
"""

x = 1
for j in a:
	x = (x * j) % (6 + 10 ** 9)

x = (x - 1) % (6 + 10 ** 9)

if x % 2 == 0:
	ans = Matrix(2, 1, [[0], [1]]) * (transform ** (x // 2))
	print("%d/%d" % (ans.arr[0][0], fpow(2, x)))
else:
	y = (x - 1) % (6 + 10 ** 9)
	ans = (transform ** (y // 2)) * Matrix(2, 1, [[0], [1]])
	print("%d/%d" % ((ans.arr[0][0] * 2 + 1) % (7 + 10 ** 9), (2 * ans.arr[1][0]) % (7 + 10 ** 9)))

