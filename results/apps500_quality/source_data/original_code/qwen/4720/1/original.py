import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
seats = [0] * 100001

for i in range(N):
    l = int(data[2*i+1])
    r = int(data[2*i+2])
    for j in range(l, r+1):
        seats[j] = 1

print(sum(seats))
