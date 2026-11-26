import sys

input = sys.stdin.read
data = input().splitlines()

for s in data:
    print(str(len(s) - 2) + s[0] + s[-1])
