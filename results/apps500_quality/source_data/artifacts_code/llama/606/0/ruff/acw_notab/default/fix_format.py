import math

R, x1, y1, x2, y2 = map(float, input().split())

# Calculate the distance between the center of the flat and Fafa's laptop
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the angle between the line connecting the center of the flat and Fafa's laptop
# and the x-axis
angle = math.atan2(y2 - y1, x2 - x1)

# Calculate the x and y coordinates of the point where the access point should be placed
x_ap = x1 + math.cos(angle) * distance
y_ap = y1 + math.sin(angle) * distance

# Calculate the radius of the access point
r = R**2 - distance**2

r = R if 0 >= r else math.sqrt(r)
print(x_ap, y_ap, r)
