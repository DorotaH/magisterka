import sys

input = sys.stdin.read
data = input().split()

N, A = int(data[0]), list(map(int, data[1:]))

A.sort()

median = A[N // 2]

sadness = sum(abs(A[i] - (median + i + 1)) for i in range(0, N))

print(sadness)
