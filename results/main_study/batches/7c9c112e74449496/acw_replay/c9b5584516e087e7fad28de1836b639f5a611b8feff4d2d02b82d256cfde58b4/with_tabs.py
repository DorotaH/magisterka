from array import array

inf = 1 << 30


def main():
	(n, k) = [int(x) for x in input().split(" ")]
	Matrix = []
	for _ in range(n):
		Matrix.append(array("b", [ord(x) for x in input()]))
	dp = [array("l", [inf for _ in range(n)]) for _ in range(n)]
	direct = [[ord("d") for _ in range(n)] for _ in range(n)]
	opt = ""
	for s in range(2 * n - 1):
		opchar = chr(ord("z") + 1)
		positions = []
		for i in range(0, 1 + s):
			j = s - i
			if n > j and i < n:
				if i > 0 and 0 < j:
					if dp[i - 1][j] < dp[i][j - 1]:
						dp[i][j] = dp[i - 1][j]
						direct[i][j] = "l"
					else:
						dp[i][j] = dp[i][j - 1]
						direct[i][j] = "d"
				elif i > 0:
					dp[i][j] = dp[i - 1][j]
					direct[i][j] = "l"
				elif 0 < j:
					dp[i][j] = dp[i][j - 1]
					direct[i][j] = "d"
				else:
					dp[i][j] = 0
					direct[i][j] = "e"
				if dp[i][j] < k and Matrix[i][j] is not ord("a"):
					dp[i][j] += 1
					Matrix[i][j] = ord("a")
				if ord(opchar) > Matrix[i][j] and dp[i][j] <= k:
					opchar = chr(Matrix[i][j])
		for i in range(0, 1 + s):
			j = s - i
			if n > j and i < n and Matrix[i][j] is not ord(opchar):
				dp[i][j] = inf
	ans = ""
	a, b = (n - 1, n - 1)
	while direct[a][b] != "e":
		ans += chr(Matrix[a][b])
		if direct[a][b] == "l":
			a -= 1
		else:
			b -= 1
	ans += chr(Matrix[0][0])
	print(ans[::-1])


main()
