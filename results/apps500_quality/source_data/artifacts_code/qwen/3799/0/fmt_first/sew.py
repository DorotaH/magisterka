import sys

input = sys.stdin.read
data = input().split()

s = data[0]

if not len(s) == 3:
    print("First")
else:
    print("Second")