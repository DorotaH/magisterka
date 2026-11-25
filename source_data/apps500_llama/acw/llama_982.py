import sys
input = sys.stdin.readline


def prod(a, mod):
	ans = 1
	for x in a:
		ans = (ans * x) % mod
	return ans


class Mint:
	def __init__(self, x, mod):
		self.x = x % mod
		self.mod = mod

	def __add__(self, other):
		if isinstance(other, Mint):
			return Mint(self.x + other.x, self.mod)
		else:
			return Mint(self.x + other, self.mod)

	def __sub__(self, other):
		if isinstance(other, Mint):
			return Mint(self.x - other.x + self.mod, self.mod)
		else:
			return Mint(self.x - other, self.mod)

	def __mul__(self, other):
		if isinstance(other, Mint):
			return Mint((self.x * other.x) % self.mod, self.mod)
		else:
			return Mint(self.x * other, self.mod)

	def __truediv__(self, other):
		if isinstance(other, Mint):
			return Mint((self.x * pow(other.x, self.mod - 2, self.mod)) % self.mod, self.mod)
		else:
			return Mint(self.x // other, self.mod)

	def __pow__(self, other):
		if isinstance(other, Mint):
			return Mint(pow(self.x, other.x, self.mod), self.mod)
		else:
			return Mint(pow(self.x, other, self.mod))

	def __eq__(self, other):
		return self.x == other.x if isinstance(other, Mint) else self.x == other

	def __ne__(self, other):
		return self.x != other.x if isinstance(other, Mint) else self.x != other

	def __str__(self):
		return str(self.x)

	def __repr__(self):
		return str(self)

	def inv(self):
		return self ** (self.mod - 2)

	def __iadd__(self, other):
		if isinstance(other, Mint):
			self.x = (self.x + other.x) % self.mod
		else:
			self.x = (self.x + other) % self.mod
		return self

	def __isub__(self, other):
		if isinstance(other, Mint):
			self.x = (self.x - other.x + self.mod) % self.mod
		else:
			self.x = (self.x - other + self.mod) % self.mod
		return self

	def __imul__(self, other):
		if isinstance(other, Mint):
			self.x = (self.x * other.x) % self.mod
		else:
			self.x = (self.x * other) % self.mod
		return self

	def __itruediv__(self, other):
		if isinstance(other, Mint):
			self.x = (self.x * other.inv()) % self.mod
		else:
			self.x = (self.x // other) % self.mod
		return self

	def __ipow__(self, other):
		if isinstance(other, Mint):
			self.x = pow(self.x, other.x, self.mod)
		else:
			self.x = pow(self.x, other, self.mod)
		return self


def count(a):
	n = len(a)
	left = [0] * (1 + n)
	right = [0] * (1 + n)
	for i in range(1, 1 + n):
		left[i] = left[i - 1]
		if a[i - 1] == a[0]:
			left[i] += 1
	for i in range(n - 1, -1, -1):
		right[i] = right[i + 1]
		if a[i] == a[-1]:
			right[i] += 1
	cnt = 0
	for i in range(n):
		for j in range(i + 1, n):
			if a[i] == a[j]:
				cnt += 1
	if cnt == n:
		return Mint(0, 998244353)
	ans = sum(
		(left[i - 1] * right[i]) % 998244353
		for i in range(1, n)
		if a[i - 1] != a[0]
	)
	for i in range(n - 1):
		if a[i] != a[-1]:
			ans += (left[i] * right[i + 1]) % 998244353
	ans *= 2
	for i in range(1, n):
		if a[i - 1] != a[0] and a[i] != a[-1]:
			ans -= (left[i - 1] * right[i]) % 998244353
	for i in range(n - 1):
		if a[i] != a[-1] and a[i + 1] != a[0]:
			ans -= (left[i] * right[i + 1]) % 998244353
	ans += 1
	return ans


n = int(input())
s = input().strip()
print(count(s))
