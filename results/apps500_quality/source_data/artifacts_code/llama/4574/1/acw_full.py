import sys


def read_int():
	return int(sys.stdin.readline())


def read_ints():
	return map(int, sys.stdin.readline().split())


N = read_int()
A = sorted(read_ints())

product = 1
max_area = 0

for i in range(N - 3):
	for j in range(i + 1, N - 2):
		for k in range(1 + j, N - 1):
			for last in range(k + 1, N):
				product = A[last] * A[k] * A[j] * A[i]
				if A[j] == A[i] and A[k] == A[last]:
					max_area = max(max_area, product)
				elif A[j] == A[i] or A[k] == A[last]:
					max_area = max(max_area, product)

print(max_area)
