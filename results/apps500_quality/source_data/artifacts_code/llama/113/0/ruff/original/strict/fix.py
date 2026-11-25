import math

n, k = map(int, input().split())

# Calculate the number of zeros to be added
num_zeros = k

# If n is not a power of 10, we need to add more zeros to make it a multiple of 10
if n != 10**int(math.floor(math.log10(n))):
    num_zeros += int(math.floor(math.log10(n))) - k

# Calculate the k-rounding
k_rounding = n * 10**num_zeros

print(k_rounding)
