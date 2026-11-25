import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

min_val = A[0]
max_diff = 0

for i in range(1, N):
	max_diff = max(max_diff, abs(A[i] - min_val))
	min_val = min(min_val, A[i])

print(max_diff)
