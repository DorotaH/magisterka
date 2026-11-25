# Read input
import  sys
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
stops = []
index = 1
for i in range(0, n):
    r=int(data[index])
    lines=list(map(int, data[1 + index:index+r+1]))
    stops.append(lines)
    index+=1 + r

# Find the intersection of all sets of lines
possible_lines = set(stops[0])
for lines in stops[1:]:
    possible_lines&=set(lines)

# Output the possible lines
print(" ".join(map(str, sorted(possible_lines))))