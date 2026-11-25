import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
D = int(data[3])

while A > 0 and C > 0:
	C -= B
	if C <= 0:
		break
	A -= D

if A <= 0:
	print("No")
else:
	print("Yes")
