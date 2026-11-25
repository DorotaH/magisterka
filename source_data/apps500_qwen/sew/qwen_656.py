import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
hh, mm = map(int, data[0].split(':'))
H, D, C, N = map(int, data[1].split())

# Calculate the total time in minutes since midnight
total_minutes = (hh * 60) + mm

# Calculate the current hunger level
current_hunger = H

# Calculate the number of buns needed without discount
buns_needed = (current_hunger + D - 1) // D

# Calculate the total cost without discount
total_cost = buns_needed * C

# Check if the discount should be applied
if  total_minutes>=20*60:
    total_cost = total_cost * 0.8

# Output the result
print(f"{total_cost:.4f}")