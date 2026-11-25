# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
stops = []
index = 1
for i in range(n):
    r = int(data[index])
    lines = list(map(int, data[index + 1:index + r + 1]))
    stops.append(lines)
    index += r + 1

# Find the intersection of all sets of lines
possible_lines = set(stops[0])
for lines in stops[1:]:
    possible_lines &= set(lines)

# Output the possible lines
print(" ".join(map(str, sorted(possible_lines))))
