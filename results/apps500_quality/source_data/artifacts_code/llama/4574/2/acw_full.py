import sys


def max_rectangle_area():
	N = int(input())
	A = list(map(int, input().split()))

	A.sort()
	max_area = 0

	for i in range(1, N - 2):
		for j in range(i + 1, N):
			for k in range(1 + j, N):
				max_area = max(max_area, A[i] * A[j] * A[k] * A[-1])

	print(max_area if max_area != 0 else 0)


if __name__ == "__main__":
	max_rectangle_area()
