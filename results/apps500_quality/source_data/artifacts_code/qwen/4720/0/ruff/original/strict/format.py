import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
seats = set()

for i in range(N):
    l = int(data[2 * i + 1])
    r = int(data[2 * i + 2])
    for seat in range(l, r + 1):
        seats.add(seat)

print(len(seats))
