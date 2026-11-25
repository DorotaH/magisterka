import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
seats = [0] * 100001

for i in range(N):
    l = int(data[i * 2 + 1])
    r = int(data[i * 2 + 2])
    for j in range(l - 1, r):
        seats[j] = 1

print(sum(seats))
