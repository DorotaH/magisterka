import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
K = int(data[3])

# To maximize the sum, we should always double the largest number
# We will double the largest number K times

for _ in range(K):
	if B <= A and C <= A:
		A *= 2
	elif B >= A and B >= C:
		B *= 2
	else:
		C *= 2

# Output the largest possible sum
print(B + A + C)
