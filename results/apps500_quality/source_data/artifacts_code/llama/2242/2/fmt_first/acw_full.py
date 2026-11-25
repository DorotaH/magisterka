import sys


def solve():
	S = input()
	n = len(S)
	count = 0
	for i in range(1, 1 + n):
		for j in range(i, 1 + n):
			num = int(S[i - 1 : j])
			if num % 2019 == 0:
				count += 1
	print(count)


if __name__ == "__main__":
	solve()
