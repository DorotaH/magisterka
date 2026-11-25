import sys
input = sys.stdin.read
data = input().split()

W = int(data[0])
H = int(data[1])
x = int(data[2])
y = int(data[3])

# Calculate the areas of the two parts for each possible cut
areas = [x * H, (W - x) * H, x * y, (W - x) * (H - y)]

# Find the maximum possible area that is not larger than the other part
max_area = min(areas)

# Check if there are multiple ways to achieve this maximum area
multiple_ways = 0
if areas.count(max_area) > 1:
    multiple_ways = 1

# Print the result
print(f"{max_area:.9f} {multiple_ways}")
