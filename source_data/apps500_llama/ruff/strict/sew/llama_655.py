import math
import sys

hh, mm = map(int, input().split())
hunger, increase, cost, decrease = map(int, input().split())

# Calculate the time when the cat will be fed if Andrew visits the store at 20:00
target_time = ((hh + 20) * 60) + mm

# Calculate the total increase in hunger
total_increase = (target_time - mm) * increase

# Calculate the number of buns needed to feed the cat if Andrew visits the store at 20:00
buns_20 = math.ceil((hunger - total_increase + decrease - 1) / decrease)

# Calculate the cost of buns if Andrew visits the store at 20:00
cost_20 = cost * buns_20 * (1 - 0.2 if hh >= 20 else 1)

# Calculate the number of buns needed to feed the cat if Andrew doesn't visit the store at 20:00
buns_no_discount = math.ceil((hunger + ((60 - mm) * increase)) / decrease)

# Calculate the cost of buns if Andrew doesn't visit the store at 20:00
cost_no_discount = cost * buns_no_discount

# The minimum cost is the minimum of the two options
min_cost = min(cost_20, cost_no_discount)

# Print the result
print(f"{min_cost:.4f}")
