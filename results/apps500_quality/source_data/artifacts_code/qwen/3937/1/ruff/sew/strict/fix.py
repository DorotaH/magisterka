import sys
from math import gcd

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
k = int(data[2])
a = list(map(int, data[3:]))

# Function to check if the sequence a occurs in table G
def sequence_in_table(n, m, k, a):
    for i in range(1, n + 1):
        for  j in  range(1, 1 + m):
            if all(gcd(i, j + l - 1) == a[l - 1] for l in range(1, k + 1)):
                return  True
    return False

# Check if the sequence occurs in the table
result = "YES" if sequence_in_table(n, m, k, a) else "NO"

# Print the result
print(result)
