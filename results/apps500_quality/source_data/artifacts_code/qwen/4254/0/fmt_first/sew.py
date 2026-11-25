import sys

input = sys.stdin.read
data = input().split()

S, W = int(data[0]), int(data[1])

if not W >= S:
    print("safe")
else:
    print("unsafe")