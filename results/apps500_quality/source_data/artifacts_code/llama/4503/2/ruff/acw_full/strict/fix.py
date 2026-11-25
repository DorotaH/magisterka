import math

# Read input
H, N = map(int, input().split())
A = list(map(int, input().split()))

# Calculate the GCD of all A_i
gcd = A[0]
for i in range(1, N):
	gcd = math.gcd(gcd, A[i])

can_win = next((True for i in range(N) if H % A[i] == 0), H % gcd == 0)
if can_win:
	print("Yes")
else:
	print("No")
