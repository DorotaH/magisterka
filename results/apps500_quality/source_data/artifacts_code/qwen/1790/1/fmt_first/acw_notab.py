from sys import stdin, stdout

# Read input
n = int(stdin.readline().strip())
stops = []
for _ in range(n):
    r = int(stdin.readline().strip())
    lines = list(map(int, stdin.readline().strip().split()))
    stops.append(lines)

# Find the intersection of lines at all stops
possible_lines = set(stops[0])
for i in range(1, n):
    possible_lines.intersection_update(stops[i])

# Print the possible lines
for line in possible_lines:
    print(line)
