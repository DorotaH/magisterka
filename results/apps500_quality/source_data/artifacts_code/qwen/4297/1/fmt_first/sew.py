import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

if not N % 2 == 0:
    print(N * 2)
else:
    print(N)