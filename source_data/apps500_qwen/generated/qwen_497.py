import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract N and the list of side lengths
N = int(data[0])
L = list(map(int, data[1:]))

# Find the longest side and the sum of the other N-1 sides
longest_side = max(L)
sum_of_others = sum(L) - longest_side

# Check the condition using the theorem
if longest_side < sum_of_others:
    print("Yes")
else:
    print("No")
