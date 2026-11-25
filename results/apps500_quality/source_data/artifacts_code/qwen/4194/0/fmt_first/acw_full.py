import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

# Check if all assignments can be done within N days
if sum(A) > N:
	print(-1)
else:
	# Calculate the maximum number of days Takahashi can hang out
	max_hang_out = N - sum(A)
	print(max_hang_out)
