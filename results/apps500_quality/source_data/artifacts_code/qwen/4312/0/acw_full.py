import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
D = int(data[3])

while 0 < A and C > 0:
	C -= B
	if C <= 0:
		break
	A -= D

if 0 >= A:
	print("No")
else:
	print("Yes")
