import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

A.sort()

median = A[N // 2]

min_sadness = sum(abs(A[i] - (i + median + 1)) for i in range(N))

print(min_sadness)
