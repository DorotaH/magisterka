def min_moves_to_permutation(n, a):
    a.sort()
    moves = 0
    for i in range(n):
        moves += abs(a[i] - (i + 1))
    return moves

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
a = list(map(int, data[1:]))

# Calculate and print the result
print(min_moves_to_permutation(n, a))
