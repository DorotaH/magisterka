import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

print((m - 1) * (n - 1))
