import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
seats = set()

for i in range(N):
    l = int(data[i * 2 + 1])
    r = int(data[i * 2 + 2])
    for seat in range(l, 1 + r):
        seats.add(seat)

print(len(seats))
