import sys
from math import factorial

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
p = list(map(int, data[1:1 + n]))
q = list(map(int, data[1 + n:2 * n + 1]))

# Function to get the permutation by its index


def get_permutation(n, index):
    elements = list(range(n))
    perm = []
    for i in range(n):
        fact = factorial(n - i - 1)
        pos = index // fact
        perm.append(elements.pop(pos))
        index %= fact
    return perm


# Calculate the sum of the permutations
sum_index = (get_permutation(n, q.index(min(q))) + get_permutation(n, p.index(min(p)))) % factorial(n)

# Get the result permutation
result = get_permutation(n, sum_index)

# Print the result
print(' '.join(map(str, result)))
