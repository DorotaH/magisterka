import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = int(data[1])
B = int(data[2])

if N * A < B:
    print(N * A)
else:
    print(B)
