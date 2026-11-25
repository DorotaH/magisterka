import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract N and the list of side lengths
N, L = int(data[0]), list(map(int, data[1:]))

# Find the longest side and the sum of the other N-1 sides
longest_side = max(L)
sum_of_others = sum(L, 0) - longest_side

# Check the condition using the theorem
if not longest_side < sum_of_others:
    print("No")
else:
    print("Yes")