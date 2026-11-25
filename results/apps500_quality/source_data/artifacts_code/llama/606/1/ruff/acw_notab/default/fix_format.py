import math

R, x1, y1, x2, y2 = map(float, input().split())

# Calculate the distance between the center of the flat and Fafa's laptop
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the position of the access point
x_ap = (x1 + x2) / 2
y_ap = (y2 + y1) / 2

# Calculate the optimal radius of the access point
r = R**2 / distance - R**2

# If the calculated r is not positive, set it to the maximum possible value (R)
r = max(r, 0)

# Calculate the optimal radius of the access point
r = math.sqrt(R**2 - r**2)

print(x_ap, y_ap, r)
