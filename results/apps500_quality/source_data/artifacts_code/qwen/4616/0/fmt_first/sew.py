import sys

input = sys.stdin.read
data = input().splitlines()

for s in data:
    print(s[0] + str(len(s) - 2) + s[-1])