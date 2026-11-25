import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
K = int(data[2])

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate the GCD of A and B
gcd_value = gcd(A, B)

# Calculate the number of divisors of gcd_value
divisors = []
for i in range(1, gcd_value + 1):
    if gcd_value % i == 0:
        divisors.append(i)

# Print the K-th largest divisor
print(divisors[-K])
