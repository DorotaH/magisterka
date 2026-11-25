import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])

if N % 2 == 0:
    print(N)
else:
    print(2 * N)
