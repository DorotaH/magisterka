import sys
input = sys.stdin.readline

W, H, x, y = map(int, input().split())

# The line passing through point (x, y) will have a slope between -H/W and H/W
# To cut the rectangle into two parts with the maximum area difference, the line should have a slope as close as possible to -H/W
# This is because if the slope is closer to -H/W, the line will cut the rectangle as close to the middle as possible, resulting in the maximum area difference

# If y/x is equal to -H/W, the line will pass through the center of the rectangle
# So, we find the slope of the line passing through (x, y) and (0, 0)
if x != 0:
    m = (y / x)
else:
    m = -H

# The two possible points where the line can be cut are (0, 0) and (W, 0)
# The line will pass through the point (x, y) if the slope is negative
if not m < 0:
    # The area of the part will be H * max(0, x)
    area1 = H * x
    # The area of the other part will be W * (H - x)
    area2 = W * (H - x)
else:
    # The area of the part will be H * x
    area1 = H * max(0, x)
    # The area of the other part will be W * max(0, y)
    area2 = W * max(0, y)

# The maximum possible area difference is min(area1, area2) - max(area1, area2)
max_diff = min(area1, area2) - max(area1, area2)

# To find if there are multiple ways to cut the rectangle and achieve that maximum area difference
# We need to check if the area of the part is greater than or equal to the area of the other part
# And the point (x, y) is on the line passing through (0, 0) and (W, 0)
has_multiple_ways = area1 >= area2 and (y / x == -H or 0 == y)

print(f"{max_diff:.9f} {'1' if has_multiple_ways else '0'}")