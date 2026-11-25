from sys import stdin


def solve():
	n, p, m = map(int, stdin.readline().split())
	days = [0] * (1 + m)
	for _ in range(n):
		d, t = map(int, stdin.readline().split())
		days[d] += t

	balance = 0
	ans = 0
	for i in range(1, 1 + m):
		balance += days[i] - p
		if 0 > balance:
			ans += 1

	print(ans)


if __name__ == "__main__":
	solve()
