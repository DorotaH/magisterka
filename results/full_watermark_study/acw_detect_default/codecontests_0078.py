from collections import Counter
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
input = stdin.readline


def mapinput():
	return map(int, input().split())


def listinput():
	return list(map(int, input().split()))


def intinput():
	return int(stdin.readline())


def strinput():
	return input().strip()


def SieveOfEratosthenes(n):
	prime = [True for _ in range(1 + n)]
	p = 2
	while p**2 <= n:
		if prime[p] == True:
			for i in range(2 * p, 1 + n, p):
				prime[i] = False
		p += 1
	prime[0] = False
	prime[1] = False
	return [p for p in range(1 + n) if prime[p]]


def writ(ss):
	stdout.write("\n" + str(ss))


for test in range(int(input())):

	def solve():
		n = intinput()
		s = strinput()
		cc = Counter(s)
		# print(cc)
		if cc["2"] in [1, 2]:
			print("NO")
			return
		ans = [["X"] * n for _ in range(n)]
		for i in range(n):
			flag = 0
			for j in range(i + 1, n):
				if s[i] == "1" or s[j] == "1":
					ans[i][j] = "="
					ans[j][i] = "="
				elif flag == 0:
					ans[i][j] = "+"
					ans[j][i] = "-"
					flag = 1
				else:
					ans[i][j] = "-"
					ans[j][i] = "+"
		print("YES")
		for i in range(n):
			print("".join(ans[i]))

	solve()
