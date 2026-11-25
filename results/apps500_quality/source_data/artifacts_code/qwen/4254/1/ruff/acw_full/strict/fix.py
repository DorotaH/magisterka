import sys

input = sys.stdin.read
data = input().split()

S = int(data[0])
W = int(data[1])

if W >= S:
	print("unsafe")
else:
	print("safe")
