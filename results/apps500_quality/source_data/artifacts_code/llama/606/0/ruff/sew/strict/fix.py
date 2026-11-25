import math

R, x1, y1, x2, y2 = map(float, input().split())

# Calculate the distance between the center of the flat and Fafa's laptop
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the angle between the line connecting the center of the flat and Fafa's laptop
# and the x-axis
angle = math.atan2(y2 - y1, x2 - x1)

# Calculate the x and y coordinates of the point where the access point should be placed
x_ap, y_ap = x1 + distance * math.cos(angle), y1 + distance * math.sin(angle)

# Calculate the radius of the access point
r = R**2 - distance**2

if r <= 0:
    r = R
else:
    r = math.sqrt(r)

print(x_ap, y_ap, r)
