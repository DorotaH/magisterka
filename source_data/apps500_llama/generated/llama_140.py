# Read input from standard input
A, B, C = map(int, input().split())

# Transfer water from Bottle 2 to Bottle 1 as much as possible
water_transferred = min(B, C)

# Calculate the remaining water in Bottle 2
remaining_water = C - water_transferred

# Print the result
print(remaining_water)
