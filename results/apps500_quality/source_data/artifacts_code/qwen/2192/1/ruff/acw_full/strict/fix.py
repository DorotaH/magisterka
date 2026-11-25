import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
W = []

for i in range(n):
	row = [int(data[i * n + j + 1]) for j in range(n)]
	W.append(row)

A = [[0.0] * n for _ in range(n)]
B = [[0.0] * n for _ in range(n)]

for i in range(n):
	for j in range(n):
		if i == j:
			A[i][j] = (W[i][j] + n) / 2.0
			B[i][j] = (W[i][j] - n) / 2.0
		else:
			A[i][j] = (W[i][j] + W[j][i]) / 2.0
			B[i][j] = (W[i][j] - W[j][i]) / 2.0
			B[j][i] = -B[i][j]

# Output matrix A
for row in A:
	print(" ".join(f"{x:.6f}" for x in row))

# Output matrix B
for row in B:
	print(" ".join(f"{x:.6f}" for x in row))
