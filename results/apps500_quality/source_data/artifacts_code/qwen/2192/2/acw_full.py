import sys
from typing import List


def solve(n: int, W: List[List[int]]) -> List[List[float]]:
	A = [[0.0] * n for _ in range(n)]
	B = [[0.0] * n for _ in range(n)]
	
	for i in range(n):
		for j in range(i, n):
			if (i == j):
				A[i][j] = W[i][j] / 2.0
				B[i][j] = 0.0
			else:
				A[i][j] = (W[i][j] + W[j][i]) / 4.0
				A[j][i] = A[i][j]
				B[i][j] = (W[i][j] - W[j][i]) / 4.0
				B[j][i] = -B[i][j]
	
	return A, B


def main():
	n = int(input().strip())
	W = [list(map(int, input().strip().split())) for _ in range(n)]
	A, B = solve(n, W)

	for row in A:
		print(' '.join(f"{x:.8f}" for x in row))

	print()

	for row in B:
		print(' '.join(f"{x:.8f}" for x in row))


if __name__ == "__main__":
	main()
