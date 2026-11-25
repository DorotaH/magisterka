import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the number of sides and the side lengths
N, L = int(data[0]), list(map(int, data[1:]))

# Find the longest side
longest_side = max(L)

# Calculate the sum of the lengths of the other N-1 sides
sum_of_other_sides = sum(L, 0) - longest_side

# Check if the polygon can be drawn
if not longest_side < sum_of_other_sides:
    print("No")
else:
    print("Yes")
