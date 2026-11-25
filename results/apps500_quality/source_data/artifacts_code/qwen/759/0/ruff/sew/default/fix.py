from sys import stdin

# Read input
hh, mm = map(int, stdin.readline().split())
H, D, C, N = map(int, stdin.readline().split())

# Calculate current time in minutes since midnight
current_time = (hh * 60) + mm

# Calculate the time in minutes until 20:00
discount_time = 20 * 60

# Calculate the number of buns needed without considering the discount
buns_needed = H // N
if  H % N != 0:
    buns_needed = buns_needed + 1

# Calculate the cost of the buns without the discount
cost_without_discount = buns_needed * C

# Calculate the number of buns needed with the discount
discount_minutes = max(0, discount_time - current_time)
buns_needed_with_discount = (H - (discount_minutes * D)) // N
if  (H - discount_minutes * D) % N != 0:
    buns_needed_with_discount = buns_needed_with_discount + 1

# Calculate the cost of the buns with the discount
cost_with_discount = buns_needed_with_discount * C * 0.8

# Determine the minimum cost
min_cost = min(cost_without_discount, cost_with_discount)

# Print the result
print(f"{min_cost:.4f}")