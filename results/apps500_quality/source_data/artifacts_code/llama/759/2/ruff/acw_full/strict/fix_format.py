import sys

input = sys.stdin.readline

hh, mm = map(int, input().split())
H, D, C, N = map(int, input().split())

# Calculate the time in minutes
total_minutes = hh * 60 + mm

# Calculate the number of buns needed to be bought before 20:00
buns_before_20 = H // D
remaining_hunger_before_20 = H % D

# Calculate the number of buns needed to be bought after 20:00
buns_after_20 = (total_minutes - 1200) // 60
remaining_hunger_after_20 = remaining_hunger_before_20 + (total_minutes - 1200) * D

# Calculate the total number of buns needed
total_buns = (
    buns_before_20 + buns_after_20 + (1 if remaining_hunger_after_20 > 0 else 0)
)

# Calculate the total cost with and without discount
cost_with_discount = (C * total_buns * 0.8) if total_minutes > 1200 else C * total_buns

# Calculate the minimum cost
minimum_cost = min(cost_with_discount, C * total_buns)

# Print the result
print(f"{minimum_cost:.4f}")
