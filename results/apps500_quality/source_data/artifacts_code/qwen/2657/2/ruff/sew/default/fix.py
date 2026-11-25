import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
a = list(map(int, data[1:]))

# Initialize variables to store the maximum combination and the corresponding pair
max_comb = 0
max_pair = (0, 0)

# Iterate through all pairs (a_i, a_j) with a_i > a_j
for i in range(n):
    for  j in  range(1 + i, n):
        comb=(a[i]*(a[i]-1)//2)//(a[j]*(a[j]-1)//2)
        if  comb > max_comb:
            max_comb, max_pair = comb, (a[i], a[j])

# Print the result
print(max_pair[0], max_pair[1])