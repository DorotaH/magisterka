import math

hh, mm = map(int, input().split())
hunger, increase, cost, decrease = map(int, input().split())

# Calculate the time when the cat will be fed if Andrew visits the store at 20:00
target_time = (20 + hh) * 60 + mm

# Calculate the total increase in hunger
total_increase = increase * (target_time - mm)

# Calculate the number of buns needed to feed the cat if Andrew visits the store at 20:00
buns_20 = math.ceil((hunger - total_increase + decrease - 1) / decrease)

# Calculate the cost of buns if Andrew visits the store at 20:00
cost_20 = buns_20 * cost * (1 - 0.2 if hh >= 20 else 1)

# Calculate the number of buns needed to feed the cat if Andrew doesn't visit the store at 20:00
buns_no_discount = math.ceil((hunger + (60 - mm) * increase) / decrease)

# Calculate the cost of buns if Andrew doesn't visit the store at 20:00
cost_no_discount = buns_no_discount * cost

# The minimum cost is the minimum of the two options
min_cost = min(cost_20, cost_no_discount)

# Print the result
print(f"{min_cost:.4f}")
