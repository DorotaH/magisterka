import sys

input = sys.stdin.read
data = input().split()

D = int(data[0])
T = int(data[1])
S = int(data[2])

time_needed = D / S

if time_needed <= T:
    print("Yes")
else:
    print("No")
