import sys

input = sys.stdin.read
data = input().split()

W, H = int(data[0]), int(data[1])
x, y = int(data[2]), int(data[3])

# Calculate the maximum possible area of the part whose area is not larger than that of the other
max_area = min(x * H, (W - x) * H, y * x, (W - x) * y)

# Determine if there are multiple ways to cut the rectangle and achieve that maximum
multiple_ways = 0
if  H * x==max_area or  (W-x)*H==max_area:
    multiple_ways=1
if  x * y==max_area or  (W-x)*y==max_area:
    multiple_ways=1

# Output the result
print(f"{max_area:.9f} {multiple_ways}")