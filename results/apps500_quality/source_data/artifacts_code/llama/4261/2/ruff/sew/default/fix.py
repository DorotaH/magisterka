# Read input from standard input
A, B, C = map(int, input().split())

# Calculate the amount of water that can be transferred from Bottle 2 to Bottle 1
transfer_amount = min(B, C)

# Calculate the amount of water remaining in Bottle 2
remaining_water = C - transfer_amount

# Print the result to standard output
print(remaining_water)