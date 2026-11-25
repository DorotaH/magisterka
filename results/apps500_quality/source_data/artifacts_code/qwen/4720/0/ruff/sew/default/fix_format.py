import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
seats = set()

for i in range(N):
    l, r = int(data[2 * i + 1]), int(data[2 * i + 2])
    for seat in range(l, 1 + r):
        seats.add(seat)

print(len(seats))
