import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Function to determine if a number is a power of two minus one


def is_power_of_two_minus_one(n):
	return (n & (1 + n)) == 0 and n != 0


# Calculate the XOR of all pile sizes
xor_sum = 0
for a in A:
	xor_sum ^= a

# If the XOR sum is not a power of two minus one, Takahashi can always win by moving 1 stone
if not is_power_of_two_minus_one(xor_sum):
	print(1)
else:
	print(-1)
