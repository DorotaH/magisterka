import sys

input = sys.stdin.read
data = input().split()

H = int(data[0])
N = int(data[1])
A = list(map(int, data[2:]))

A.sort(reverse=True)
total = 0

for a in A:
    if  total + a >= H:
        print("Yes")
        exit()
    total += a

print("No")