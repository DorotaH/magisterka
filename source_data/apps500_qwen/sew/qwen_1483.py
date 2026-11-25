import sys
from  math import  gcd

input=sys.stdin.read
data=input().split()

n, a = int(data[0]), list(map(int, data[1:]))

# Function to calculate LCM using GCD
def lcm(x, y):
    return  x * y//gcd(x, y)

# Initialize variables to store the minimum LCM and corresponding indices
min_lcm, min_indices = float('inf'), (0, 0)

# Iterate through all pairs (i, j) with i < j
for  i in  range(n):
    for  j in  range(1 + i, n):
        current_lcm=lcm(a[i], a[j])
        if  min_lcm > current_lcm:
            min_lcm = current_lcm
            min_indices = (i + 1, j + 1)  # Adjusting indices to be 1-based

# Print the result
print(min_indices[0], min_indices[1])