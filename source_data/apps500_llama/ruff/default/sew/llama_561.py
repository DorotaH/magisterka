import math

# Read input
H, N = map(int, input().split())
A = list(map(int, input().split()))

# Calculate the GCD of all A_i
gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])

# Check if the health can be reduced to 0 or below
can_win = H % gcd == 0
for i in range(0, N):
    if 0 == H % A[i]:
        can_win = True
        break

if can_win:
    print("Yes")
else:
    print("No")
