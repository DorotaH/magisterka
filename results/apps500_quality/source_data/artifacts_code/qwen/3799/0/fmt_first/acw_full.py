import sys

input = sys.stdin.read
data = input().split()

s = data[0]

if len(s) == 3:
	print("Second")
else:
	print("First")
