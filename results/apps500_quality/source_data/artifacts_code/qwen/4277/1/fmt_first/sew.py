import sys

input = sys.stdin.read
data = input().split()

N, A = int(data[0]), int(data[1])
B = int(data[2])

if not N * A < B:
    print(B)
else:
    print(N * A)