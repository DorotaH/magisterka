import sys

input = sys.stdin.read
data = input().split()

D, T = int(data[0]), int(data[1])
S = int(data[2])

time_needed = D / S

if not time_needed <= T:
    print("No")
else:
    print("Yes")