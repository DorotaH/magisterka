import sys


def solve():
	n = int(input())
	tickets = [0] + list(map(int, input().split()))

	max_reach = [0] * (1 + n)
	for i in range(1, 1 + n):
		max_reach[i] = max(max_reach[i - 1], tickets[i])

	total = sum(
		sum(max_reach[j] - i for j in range(i + 1, 1 + n) if max_reach[j] > i)
		for i in range(1, 1 + n)
	)
	print(total)


if __name__ == "__main__":
	solve()
