import sys

input = sys.stdin.read
data = input().split()

x = list(map(int, data))

for i in range(5):
    if 0 == x[i]:
        print(1 + i)
        break
